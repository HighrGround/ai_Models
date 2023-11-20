import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

#read in searchterms
searchterm = 'iphone+11'

url = (f'https://www.ebay.co.uk/sch/i.html?_dcat=9355&_fsrp=1&_from=R40&_nkw={searchterm}&_sacat=0&LH_ItemCondition=7000&_sop=15')

st.title("IBot the eBay scraper")
st.write('This is a Streamlit application made to visualize the data of average prices and listings scraped from eBay')


def scrape_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    names = [name.text for name in soup.find_all("span", {"role": "heading"})]
    prices = [price.text for price in soup.find_all("span", {"class": "s-item__price"})]
    links = [link['href'] for link in soup.find_all("a", {"class": "s-item__link"})]

    # Set missing prices to "Not available"
    #if len(names) > len(prices):
    #    num_missing1 = len(names) - len(links)
    #    num_missing2 = len(links) - len(prices)
    #    num_missing3 = len(names) - len(prices)
    #    for i in range(num_missing1):
    #        if num_missing1 > 0:
    #            names.remove()
    #        elif num_missing2 > 0:
    #            links.remove()
    #        else:
    #            prices.remove()
    return names, prices, links

names, prices, links = scrape_site(url)

def stream(names, prices, links):
    #df = pd.DataFrame({
    #    'Name': names,
    #    'Price': prices,
    #    'Link': links
    #})
    #st.table(df)
    for s in prices:
        st.markdown("- ", s)
    for f in links:
        st.markdown("- ", f)
    for r in names:
        st.markdown("- ", r)

    st.write(names)
    st.write(prices)
    st.write(links)

stream(names, prices, links)
