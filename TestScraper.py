## Import Libraries

import csv
import pandas as pd
import asyncio
import time

from arsenic import get_session, browsers, services
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup




links = []



## Get the data from CSV file

Tesco_Taxonomy = csv.DictReader(open("Asda_Taxonomy.csv"))


def page(body):
    
    soup = BeautifulSoup(body, 'lxml')
    data = soup.select('#main-content > main > div:nth-child(2) > div > div:nth-child(4) > div > div.search-pagination > div.co-pagination > a.asda-btn.asda-btn--clear.co-pagination__arrow.co-pagination__arrow--right')
    print(data)
   



async def scraper(url):
    
    limit = asyncio.Semaphore(10)
    
    service = services.Chromedriver(binary = ChromeDriverManager().install())
    browser = browsers.Chrome()
    ## Not running headless for testing, change later
    # browser.capabilities = { 'goog:chromeOptions': {"args": ['--disable-gpu', '--headless=new', '--no-sandbox', '--disable-dev-shm-usage']}}
    browser.capabilities = { 'goog:chromeOptions': {"args": ['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']}}   
    async with limit:
        
        async with get_session(service, browser) as session:
            
            await session.get(url)
            body = await session.get_page_source()
            
    
    



async def page(Tesco_Taxonomy):

    for page_ID in Tesco_Taxonomy:
        
        
        
        if page_ID.get('shelve_name') != '':
        
        
            #print(type(page_ID.get('shleve_hierarchy_ID')))
            link = (page_ID.get('shleve_hierarchy_ID'))
            url = f'https://groceries.asda.com/shelf/home-entertainment/toys/toys-by-minimum-age/ages-0-months/{link}'
            
            await scraper(url)
            
        else:
            
            link = (page_ID.get('aisle_hierarchy_ID'))
            
            url = f'https://groceries.asda.com/shelf/home-entertainment/toys/toys-by-minimum-age/ages-0-months/{link}'
            
            await scraper(url)
            
            
if __name__ == '__main__':
    
    start = time.time()
    asyncio.run(page(Tesco_Taxonomy))
    end = time.time() - start
    print(f'total time is: {end}')