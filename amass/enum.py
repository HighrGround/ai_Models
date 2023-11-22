import argparse
import os
import sys
import time
import signal
import subprocess
from enum import Enum, auto
from typing import List, Set, Optional

class EnumOptions(Enum):
    ACTIVE = auto()
    ALTERATIONS = auto()
    BRUTE_FORCING = auto()
    DEMO_MODE = auto()
    LIST_SOURCES = auto()
    NO_ALTS = auto()
    NO_COLOR = auto()
    NO_RECURSIVE = auto()
    PASSIVE = auto()
    SILENT = auto()
    VERBOSE = auto()

class EnumArgs:
    def __init__(self):
        self.Addresses: List[str] = []
        self.ASNs: List[int] = []
        self.CIDRs: List[str] = []
        self.AltWordList: Set[str] = set()
        self.AltWordListMask: Set[str] = set()
        self.BruteWordList: Set[str] = set()
        self.BruteWordListMask: Set[str] = set()
        self.Blacklist: Set[str] = set()
        self.Domains: Set[str] = set()
        self.Excluded: Set[str] = set()
        self.Included: Set[str] = set()
        self.Interface: str = ""
        self.MaxDNSQueries: int = 0
        self.ResolverQPS: int = 0
        self.TrustedQPS: int = 0
        self.MaxDepth: int = 0
        self.MinForRecursive: int = 1
        self.Names: Set[str] = set()
        self.Ports: List[int] = [80, 443]
        self.Resolvers: Set[str] = set()
        self.Trusted: Set[str] = set()
        self.Timeout: int = 0
        self.Options = {
            EnumOptions.ACTIVE: False,
            EnumOptions.ALTERATIONS: False,
            EnumOptions.BRUTE_FORCING: False,
            EnumOptions.DEMO_MODE: False,
            EnumOptions.LIST_SOURCES: False,
            EnumOptions.NO_ALTS: False,
            EnumOptions.NO_COLOR: False,
            EnumOptions.NO_RECURSIVE: False,
            EnumOptions.PASSIVE: False,
            EnumOptions.SILENT: False,
            EnumOptions.VERBOSE: False,
        }
        self.Filepaths = {
            "AllFilePrefix": "",
            "AltWordlist": [],
            "Blacklist": "",
            "BruteWordlist": [],
            "ConfigFile": "",
            "Directory": "",
            "Domains": [],
            "ExcludedSrcs": "",
            "IncludedSrcs": "",
            "JSONOutput": "",
            "LogFile": "",
            "Names": [],
            "Resolvers": [],
            "ScriptsDirectory": "",
            "TermOut": "",
        }

    def __str__(self):
        return f"EnumArgs: {vars(self)}"

def define_enum_argument_flags(enum_flags, args):
    enum_flags.add_argument('--addr', dest='Addresses', action='append', help='IPs and ranges (192.168.1.1-254) separated by commas')
    enum_flags.add_argument('--asn', dest='ASNs', type=int, action='append', help='ASNs separated by commas')
    enum_flags.add_argument('--cidr', dest='CIDRs', action='append', help='CIDRs separated by commas')
    enum_flags.add_argument('--awm', dest='AltWordListMask', action='append', help='"hashcat-style" wordlist masks for name alterations')
    enum_flags.add_argument('--wm', dest='BruteWordListMask', action='append', help='"hashcat-style" wordlist masks for DNS brute forcing')
    enum_flags.add_argument('--bl', dest='Blacklist', action='append', help='Blacklist of subdomain names that will not be investigated')
    enum_flags.add_argument('--d', dest='Domains', action='append', help='Domain names separated by commas')
    enum_flags.add_argument('--exclude', dest='Excluded', action='append', help='Data source names separated by commas to be excluded')
    enum_flags.add_argument('--include', dest='Included', action='append', help='Data source names separated by commas to be included')
    enum_flags.add_argument('--iface', dest='Interface', help='Provide the network interface to send traffic through')
    enum_flags.add_argument('--dns-qps', dest='ResolverQPS', type=int, help='Maximum number of DNS queries per second for each untrusted resolver')
    enum_flags.add_argument('--trqps', dest='TrustedQPS', type=int, help='Maximum number of DNS queries per second for each trusted resolver')
    enum_flags.add_argument('--max-depth', dest='MaxDepth', type=int, help='Maximum number of subdomain labels for brute forcing')
    enum_flags.add_argument('--min-for-recursive', dest='MinForRecursive', type=int, default=1, help='Subdomain labels seen before recursive brute forcing (Default: 1)')
    enum_flags.add_argument('--p', dest='Ports', type=int, action='append', help='Ports separated by commas (default: 80, 443)')
    enum_flags.add_argument('--r', dest='Resolvers', action='append', help='IP addresses of untrusted DNS resolvers (can be used multiple times)')
    enum_flags.add_argument('--tr', dest='Trusted', action='append', help='IP addresses of trusted DNS resolvers (can be used multiple times)')
    enum_flags.add_argument('--timeout', dest='Timeout', type=int, help='Number of minutes to let enumeration run before quitting')

def define_enum_option_flags(enum_flags, args):
    enum_flags.add_argument('--active', dest='Options', action='store_true', help='Attempt zone transfers and certificate name grabs')
    enum_flags.add_argument('--alterations', dest='Options', action='store_true', help='Enable generation of altered names')
    enum_flags.add_argument('--brute', dest='Options', action='store_true', help='Execute brute forcing after searches')
    enum_flags.add_argument('--demo', dest='Options', action='store_true', help='Censor output to make it suitable for demonstrations')
    enum_flags.add_argument('--list', dest='Options', action='store_true', help='Print the names of all available data sources')
    enum_flags.add_argument('--noalts', dest='Options', action='store_true', help='Disable alterations')
    enum_flags.add_argument('--nocolor', dest='Options', action='store_true', help='Disable colorized output')
    enum_flags.add_argument('--norecursive', dest='Options', action='store_true', help='Turn off recursive brute forcing')
    enum_flags.add_argument('--passive', dest='Options', action='store_true', help='Deprecated since passive is the default setting')
    enum_flags.add_argument('--silent', dest='Options', action='store_true', help='Disable all output during execution')
    enum_flags.add_argument('-v', dest='Options', action='store_true', help='Output status / debug / troubleshooting info')

def define_enum_filepath_flags(enum_flags, args):
    enum_flags.add_argument('-oA', dest='Filepaths["AllFilePrefix"]', help='Path prefix used for naming all output files')
    enum_flags.add_argument('-aw', dest='Filepaths["AltWordlist"]', action='append', help='Dictionary file for name alterations')
    enum_flags.add_argument('-b', dest='Filepaths["Blacklist"]', help='Blacklist source file')
    enum_flags.add_argument('-w', dest='Filepaths["BruteWordlist"]', action='append', help='Dictionary file for DNS brute forcing')
    enum_flags.add_argument('-c', dest='Filepaths["ConfigFile"]', help='Configuration file for alter options')
    enum_flags.add_argument('-d2', dest='Filepaths["Directory"]', help='Path to the directory containing Enumerations.csv')
    enum_flags.add_argument('-enum', dest='Filepaths["Domains"]', action='append', help='Data source enumeration file')
    enum_flags.add_argument('-exclude-sources', dest='Filepaths["ExcludedSrcs"]', help='File containing data source names that are not of interest')
    enum_flags.add_argument('-exclude', dest='Filepaths["Excluded"]', help='File containing subdomain names that will not be investigated')
    enum_flags.add_argument('-include-sources', dest='Filepaths["IncludedSrcs"]', help='File containing data source names to be investigated')
    enum_flags.add_argument('-include', dest='Filepaths["Included"]', help='File containing subdomain names to be investigated')
    enum_flags.add_argument('-json', dest='Filepaths["JSONOutput"]', help='File where data will be written in JSON format')
    enum_flags.add_argument('-log', dest='Filepaths["LogFile"]', help='File to which all screen output should be written')
    enum_flags.add_argument('-p', dest='Filepaths["Names"]', action='append', help='File containing new line delimited subdomain names')
    enum_flags.add_argument('-r', dest='Filepaths["Resolvers"]', action='append', help='File containing IP addresses of untrusted DNS resolvers')
    enum_flags.add_argument('-s', dest='Filepaths["ScriptsDirectory"]', help='Path to a directory full of Perl scripts')
    enum_flags.add_argument('-t', dest='Filepaths["TermOut"]', help='File where terminal out will be written')

def main():
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser()
    args = EnumArgs()
    
    # Define flags for arguments, options, and filepaths
    define_enum_argument_flags(parser, args)
    define_enum_option_flags(parser, args)
    define_enum_filepath_flags(parser, args)

    # Parse the command line arguments
    results = parser.parse_args()

if __name__ == "__main__":
    main()