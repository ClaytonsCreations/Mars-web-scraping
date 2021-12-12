from bs4 import BeautifulSoup
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    scraped_data = {}


# # NASA Mars News
# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

# Examine the results, then determine element that contains sought info
print(soup.prettify())

results = soup.find_all('div', class_='slide')
print(results)

for result in results:
    try:
        title = result.find('div', 'content_title')
        news_title = title.a.text
        news = result.find('div', 'rollover_description_inner')
        news_p = news.text
        
        if(news_title and news_p):
            print('-----------')
            print(news_title)
            print(news_p)
            
    except AttributeError as e:
        print(e)


# # JPL Mars Space Images - Featured Image
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

mars_url = 'https://spaceimages-mars.com/'
browser.visit(mars_url)

# Parse HTML with Beautiful Soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

button = image_soup.find('a', class_="showimg fancybox-thumbs")

# Parse HTML with Beautiful Soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

browser.find_by_text(' FULL IMAGE').click()

# image_url = image_soup.find('img', class_="fancybox-image")
image_url = image_soup.find_all('img')[1]
image_url_text = (image_url.get("src"))

featured_image_url = (f'{mars_url}{image_url_text}')


# # Mars Facts
mars_facts = 'https://galaxyfacts-mars.com/'

tables = pd.read_html(mars_facts)

mars_table = tables[1]

mars_table.columns = ['Description', 'Value']

mars_html_table = mars_table.to_html()

mars_html_table.replace('\n', '')

mars_table.to_html('mars_html_table.html')


# # Mars Hemispheres
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemispheres_url = "https://marshemispheres.com/"
browser.visit(hemispheres_url)

html_hemispheres = browser.html

soup_hem = BeautifulSoup(html_hemispheres, 'html.parser')

description = soup_hem.find_all('div', class_='item')


hemisphere_image_data = []

for hemisphere in range(len(description)):

    hem_link = browser.find_by_css("a.product-item h3")
    hem_link[hemisphere].click()
    time.sleep(1)
    
    img_detail_html = browser.html
    imagesoup = BeautifulSoup(img_detail_html, 'html.parser')
    
    base_url = {'hemispheres_url'}
    
    hem_url = imagesoup.find('img', class_="wide-image")['src']
    
    img_url = (base_url and hem_url)

    img_title = browser.find_by_css('.title').text
    
    hemisphere_image_data.append({"title": img_title, "img_url": img_url})
    browser.back()

browser.quit()

scraped_data = {
    "news_title": news_title,
    "news_p": news_p,
    "featured_image_url": featured_image_url,
    "mars_html_table": mars_html_table, 
    "hemisphere_image_data": hemisphere_image_data
}
