#!/usr/bin/env python
# coding: utf-8

#!pip install splinter

import pandas as pd
import json
from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt
import time

def scrape_all():

  # exe path for chrome to open chrome page
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_p = get_news_mars(browser)
     
    datapage = {
        "news_title":news_title,
        'news_para':news_p,
        "featured_image": get_featured_image(browser),
        "facts_html": get_mars_facts(),
        "hemisphere_image_urls": get_hemisphere_urls(browser), 
        "last_modified": dt.datetime.utcnow() 
               }
    
    # Quit browser and return all needed data
    browser.quit()
    return datapage
# Web Scraping   
# NASA Mars News scraping function
def get_news_mars(browser):
    # URL of NASA Mars site, News page to be scraped
    mars_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_url)

    # Get HTML page with the browser; create BeautifulSoup object; parse with 'html.parser'
    mars_html = browser.html
    soup = bs(mars_html, 'lxml')

    # Collect the latest News Title and Paragraph Text.
    # Assign the text to variables to be referenced later.
    try:
        news_title = soup.find('li',class_="slide").find('div', class_='content_title').text
        news_p = soup.find('div', class_='article_teaser_body').text
    except AttributeError:
        return None
    return news_title,news_p
    
# JPL Mars Space Images - Featured Image scraping function
def get_featured_image(browser):
    # URL of NASA Mars site, JPL Featured Space Images page to be scraped
    mar_space_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
   # mar_space_images_url = base_url + '/spaceimages/?search=&category=Mars'
    browser.visit(mar_space_images_url)
    time.sleep(1)

    # Find and Click "FULL IMAGE" button
    full_image_data = browser.find_by_id('full_image')
    full_image_data.click()
    time.sleep(1)

    # Find and Click 'more info' button, wait a second
    more_info_data = browser.links.find_by_partial_text('more info')
    more_info_data.click()
    time.sleep(1)

    # Find the actual website path we are going to scrape and read/show the data using BeautifulSoup
    html = browser.html
    soup = bs(html, 'lxml')

    # Find featured_image_url large size 
    try: 
        featured_image_url = soup.find('figure', class_='lede').a['href']
        featured_image_url
        #print(f"The featured_image_url is: {featured_image_url}") 
    except AttributeError:
        return None
    # Compose complete url string for full size image link
    featured_image_url_large = f'https://www.jpl.nasa.gov{featured_image_url}'
    #print(f"The full_image_url is: {featured_image_url_large}") 
    return featured_image_url_large

# Mars Facts scraping into HTML table
# Read Mars Facts webpage; use Pandas to scrape the table containing facts about the planet
def get_mars_facts():
    # Visit the url to be scraped   
    facts_url = 'http://space-facts.com/mars/'
    facts_df=pd.read_html(facts_url)[0]
    facts_df.columns = ['Description','Mars']
    facts_df['Description']=facts_df['Description'].str.replace(':','')
    facts_df.set_index('Description', inplace=True)
    facts_df
    # Convert the data to a HTML table string
    facts_df.to_html()
    # Format HTML table with bootstrap
    return facts_df.to_html(classes="table table-striped")

# Mars Hemispheres
# To obtain high resolution images for each of Mar's hemispheres
def get_hemisphere_urls(browser):
    # Find the actual website path we are going to scrape and visit the url to be scraped
    base_url = 'https://astrogeology.usgs.gov'
    url = base_url+'/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Read/show the data using BeautifulSoup
    html = browser.html
    soup = bs(html,'lxml')

    # Extracted the titles and the image browser url to extract the full resolution image by looping 
    image_urls = [(a.text, a['href']) for a in browser.find_by_css('div[class="description"] a')]
    # Initialize the list for the dictionary of hemisphere images 
    hemisphere_image_urls = []
    for title,url in image_urls:
    # Used a Python dictionary to store the data
        temp = {}
        temp['title'] = title
        # Visit the url to look for image url
        browser.visit(url)
        img_url = browser.find_by_css('img[class="wide-image"]')['src']
        temp['img_url'] = img_url
        #print(temp)
    # Appended each hemisphere info of all hemipheres to the list
        hemisphere_image_urls.append(temp)
    #print(hemisphere_image_urls)
    # Displayed titles and image links
    hemisphere_image_urls
    # Navigate back
    browser.back()
    return hemisphere_image_urls

if __name__ == "__main__":
    print(scrape_all())