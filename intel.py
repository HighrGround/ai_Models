import sys
import os
import signal
import time
import argparse
from argparse import ArgumentParser
import subprocess
from datetime import datetime
from typing import Set

class intelArgs:
    def __init__(self):
        self.Domains = set()
        self.Excluded = set()
        self.Included = set()
        self.Resolvers = set()
        self.Filepaths = {
            "ConfigFile": "",
            "Directory": "",
            "Domains": set(),
            "ExcludedSrcs": "",
            "IncludedSrcs": "",
            "LogFile": "",
            "TermOut": ""
        }
        self.Addresses = set()
        self.ASNs = set()
        self.CIDRs = set()
        self.OrganizationName = ""
        self.MaxDNSQueries = 0
        self.Ports = set()
        self.Timeout = 0
        self.Options = {
            "Active": False,
            "DemoMode": False,
            "IPs": False,
            "IPv4": False,
            "IPv6": False,
            "ListSources": False,
            "ReverseWhois": False,
            "Verbose": False
        }

def define_intel_argument_flags(intel_flags: ArgumentParser, args: intelArgs):
    intel_flags.add_argument("-addr", dest="Addresses", type=str, help="IPs and ranges (192.168.1.1-254) separated by commas")
    intel_flags.add_argument("-asn", dest="ASN", type=str, help="ASNs separated by commas (can be used multiple times)")
    intel_flags.add_argument("-cidr", dest="CIDRs", type=str, help="CIDRs separated by commas (can be used multiple times)")
    intel_flags.add_argument("-org", dest="OrganizationName", type=str, help="Search string provided against AS description information")
    intel_flags.add_argument("-d", dest="Domains", type=str, help="Domain names separated by commas (can be used multiple times)")
    intel_flags.add_argument("-exclude", dest="Excluded", type=str, help="Data source names separated by commas to be excluded")
    intel_flags.add_argument("-include", dest="Included", type=str, help="Data source names separated by commas to be included")
    intel_flags.add_argument("-max-dns-queries", dest="MaxDNSQueries", type=int, help="Maximum number of concurrent DNS queries")
    intel_flags.add_argument("-p", dest="Ports", type=str, help="Ports separated by commas (default: 80, 443)")
    intel_flags.add_argument("-r", dest="Resolvers", type=str, help="IP addresses of preferred DNS resolvers (can be used multiple times)")
    intel_flags.add_argument("-timeout", dest="Timeout", type=int, help="Number of minutes to let enumeration run before quitting")

def define_intel_option_flags(intel_flags: ArgumentParser, args: intelArgs):
    intel_flags.add_argument("--active", dest="Options['Active']", action="store_true", help="Attempt certificate name grabs")
    intel_flags.add_argument("--demo", dest="Options['DemoMode']", action="store_true", help="Censor output to make it suitable for demonstrations")
    intel_flags.add_argument("--ip", dest="Options['IPs']", action="store_true", help="Show the IP addresses for discovered names")
    intel_flags.add_argument("--ipv4", dest="Options['IPv4']", action="store_true", help="Show the IPv4 addresses for discovered names")
    intel_flags.add_argument("--ipv6", dest="Options['IPv6']", action="store_true", help="Show the IPv6 addresses for discovered names")
    intel_flags.add_argument("--list", dest="Options['ListSources']", action="store_true", help="Print additional information")
    intel_flags.add_argument("--whois", dest="Options['ReverseWhois']", action="store_true", help="All provided domains are run through reverse whois")
    intel_flags.add_argument("-v", dest="Options['Verbose']", action="store_true", help="Output status / debug / troubleshooting info")

def define_intel_filepath_flags(intel_flags: ArgumentParser, args: intelArgs):
    intel_flags.add_argument("--config", dest="Filepaths['ConfigFile']", type=str, help="Path to the YAML configuration file. Additional details below")
    intel_flags.add_argument("--dir", dest="Filepaths['Directory']", type=str, help="Path to the directory containing the output files")
    intel_flags.add_argument("--df", dest="Filepaths['Domains']", type=str, help="Path to a file providing root domain names")
    intel_flags.add_argument("--ef", dest="Filepaths['ExcludedSrcs']", type=str, help="Path to a file providing data sources to exclude")
    intel_flags.add_argument("--if", dest="Filepaths['IncludedSrcs']", type=str, help="Path to a file providing data sources to include")
    intel_flags.add_argument("--log", dest="Filepaths['LogFile']", type=str, help="Path to the log file where errors will be written")
    intel_flags.add_argument("--rf", dest="Filepaths['Resolvers']", type=str, help="Path to a file providing preferred DNS resolvers")
    intel_flags.add_argument("-o", dest="Filepaths['TermOut']", type=str, help="Path to the text file containing terminal stdout/stderr")

def run_intel_command(args):
    help1 = False
    help2 = False

    intel_flags = argparse.ArgumentParser()
    define_intel_argument_flags(intel_flags, args)
    define_intel_option_flags(intel_flags, args)
    define_intel_filepath_flags(intel_flags, args)

    if len(sys.argv) < 2:
        print("Usage: python script.py intel [options] [-whois -d DOMAIN] [-addr ADDR -asn ASN -cidr CIDR]")
        return

    parsed_args = intel_flags.parse_args()
    args = vars(parsed_args)
    if help1 or help2:
        print("Usage: python script.py intel [options] [-whois -d DOMAIN] [-addr ADDR -asn ASN -cidr CIDR]")
        return

    # Rest of the code here

def main():
    args = intelArgs()
    run_intel_command(args)

if __name__ == "__main__":
    main()
