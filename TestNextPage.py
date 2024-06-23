## Import Libraries

import csv
import pandas as pd
import asyncio
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

import AuxFunctions


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--allow-running-insecure-content')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#url = 'https://groceries.asda.com/aisle/fruit-veg-flowers/fruit/apples/1215686352935-910000975210-1215666691670'

urls = [
    #'https://groceries.asda.com/aisle/fruit-veg-flowers/fruit/apples/1215686352935-910000975210-1215666691670',
    #'https://groceries.asda.com/aisle/fruit-veg-flowers/fruit/view-all-fruit/1215686352935-910000975210-1215666947025?page=3'
    #'https://groceries.asda.com/shelf/home-entertainment/toys/toys-by-minimum-age/ages-0-months/1215684741317-1215684741318-1215686353958'
    'https://groceries.asda.com/aisle/fruit-veg-flowers/fruit/apples/1215686352935-910000975210-1215666691670'
    ]

links = []



## Get the data from CSV file

Tesco_Taxonomy = csv.DictReader(open("Asda_Taxonomy.csv"))



        
    
        
    
    
## Function to extract the data 

def find_data(url, data, next_page):
    
    a = 10
    
    for item in data:
        
        product_data = {
            'extration_date': datetime.date.today(),
            #'product_ID': product_ID,
            #'product_ID': AuxFunctions.product_code(url.get('aisle_ID'), a),
            'product_name': AuxFunctions.extract_data(item, 'a.co-product__anchor'),
            'price': AuxFunctions.extract_data(item, 'strong.co-product__price'),
            'price_per': AuxFunctions.extract_data(item, 'span.co-product__price-per-uom'),
            'saver_banner': AuxFunctions.extract_data(item, 'div.link-save-banner-large__meat-sticker'),
            'saver_banner_link': AuxFunctions.product_link(item, 'a', 'link-save-banner-large__anchor'),
            'quantity': AuxFunctions.extract_data(item, 'span.co-product__volume'),
            'label': AuxFunctions.extract_data(item, 'span.co-product__promo-text'),
            #'diet_type': AuxFunctions.labels(item, 'img', 'asda-img'),                 ## --> back later to get this tags
            #'best_before': AuxFunctions.labels(item, 'li.img'),                ## --> back later to get this tags
            #'live_better_label': AuxFunctions.labels(item, 'img.asda-img'),    ## --> back later to get this tags
            #'aldi_price_label': AuxFunctions.extract_data(item, 'p.styled__DarkGreyBodyText-jk5kya-0'),
            'product_link': AuxFunctions.product_link(item, 'a', 'co-product__anchor'),
            'product_image': AuxFunctions.product_image(item, 'source'),
            'url': url
        } 
   
   #<img alt="Fresh Same Day" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/fresh-best-same-day-icon?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="Fresh Same Day">
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on M&amp;S Taste Match"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/M-S-Taste-Match-Icon?$Icon-wapp2x$=&amp;qlt=50"><img alt="M&amp;S Taste Match" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/M-S-Taste-Match-Icon?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="M&amp;S Taste Match"></picture></button></div></li>
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on Typically fresh for 2 days"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/produce-2-days-icon?$Icon-wapp2x$=&amp;qlt=50"><img alt="Typically fresh for 2 days" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/produce-2-days-icon?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="Typically fresh for 2 days"></picture></button></div></li>
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on Live Better"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/_923_LiveBetter_Update?$Icon-wapp2x$=&amp;qlt=50"><img alt="Live Better" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/_923_LiveBetter_Update?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="Live Better"></picture></button></div></li>
        
        print('======================')
        print(product_data)
        print('££££££££££££££££££££££££££')
        print(url)
        



def check_next_page(next_page):
    
    
    
    for page in next_page[1:]:
    
        next_url = f"https://groceries.asda.com/aisle/fruit-veg-flowers/fruit/view-all-fruit/1215686352935-910000975210-1215666947025?page={page['value']}"
       
        driver.get(next_url)
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        data = soup.select('#main-content > main > div > div.co-product-list > ul > li')
                            ##main-content > main > div:nth-child(5) > div.co-product-list > ul > li:nth-child(1)
                            ##main-content > main > div:nth-child(7) > div.co-product-list > ul > li:nth-child(1)
                            ##main-content > main > div:nth-child(6) > div.co-product-list > ul > li:nth-child(1)
        find_data(next_url, data, next_page)
           
    
    
    
    
    #check_next_page(next_page)
    


def scraper(urls):
    
    
    for url in urls:
    
        
        
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        data = soup.select('#main-content > main > div:nth-child(6) > div.co-product-list > ul > li')
        next_page = soup.select('#main-content > main > div:nth-child(6) > div.page-navigation > div > div.co-dropdown.pagination-dropdown > select > option')
        
        find_data(url, data, next_page)
        
        if next_page == []:
            pass
        
        
            
            
        else:
            
            check_next_page(next_page)
        
            

        
 
            
    
    




            
            
if __name__ == '__main__':
    
    start = time.time()
    scraper(urls)
    end = time.time() - start
    print(f'total time is: {end}')