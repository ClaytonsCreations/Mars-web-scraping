{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbee8db1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a34e967e",
   "metadata": {},
   "source": [
    "# NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46ebaadb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "feaaa6cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve page with the requests module\n",
    "response = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0649cdd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup = BeautifulSoup(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "523b722c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Examine the results, then determine element that contains sought info\n",
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33959890",
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find_all('div', class_='slide')\n",
    "print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb71facb",
   "metadata": {},
   "outputs": [],
   "source": [
    "for result in results:\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    try:\n",
    "        title = result.find('div', 'content_title')\n",
    "        news_title = title.a.text\n",
    "        news = result.find('div', 'rollover_description_inner')\n",
    "        news_p = news.text\n",
    "        \n",
    "        \n",
    "        if(news_title and news_p):\n",
    "            print('-----------')\n",
    "            print(news_title)\n",
    "            print(news_p)\n",
    "            \n",
    "    except AttributeError as e:\n",
    "        print(e)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "13c1f0ea",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1c23b8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from splinter import Browser\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd5f6140",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ce8868d",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_url = 'https://spaceimages-mars.com/'\n",
    "browser.visit(mars_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b27941e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse HTML with Beautiful Soup\n",
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f37e195b",
   "metadata": {},
   "outputs": [],
   "source": [
    "button = image_soup.find('a', class_=\"showimg fancybox-thumbs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "304516cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "button"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2587339",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse HTML with Beautiful Soup\n",
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddc29026",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.find_by_text(' FULL IMAGE').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e136db02",
   "metadata": {},
   "outputs": [],
   "source": [
    "# image_url = image_soup.find('img', class_=\"fancybox-image\")\n",
    "image_url = image_soup.find_all('img')[1]\n",
    "image_url_text = (image_url.get(\"src\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67b0c2af",
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url = (f'{mars_url}{image_url_text}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebec84d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3352978f",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08e5256b",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58635ad3",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts = 'https://galaxyfacts-mars.com/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f83cf271",
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(mars_facts)\n",
    "\n",
    "mars_table = tables[1]\n",
    "mars_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a05a01c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_table.columns = ['Description', 'Value']\n",
    "mars_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3ffd06d",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_html_table = mars_table.to_html()\n",
    "mars_html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "404b1393",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_html_table.replace('\\n', '')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc41036b",
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_table.to_html('mars_html_table.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84c9a6be",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13546ece",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e516c4ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemispheres_url = \"https://marshemispheres.com/\"\n",
    "browser.visit(hemispheres_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "667c2b8b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "html_hemispheres = browser.html\n",
    "\n",
    "soup_hem = BeautifulSoup(html_hemispheres, 'html.parser')\n",
    "\n",
    "description = soup_hem.find_all('div', class_='item')\n",
    "\n",
    "description"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06e9adc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_data = []\n",
    "\n",
    "for hemisphere in range(len(description)):\n",
    "\n",
    "    hem_link = browser.find_by_css(\"a.product-item h3\")\n",
    "    hem_link[hemisphere].click()\n",
    "    time.sleep(1)\n",
    "    \n",
    "    img_detail_html = browser.html\n",
    "    imagesoup = BeautifulSoup(img_detail_html, 'html.parser')\n",
    "    \n",
    "    base_url = {'hemispheres_url'}\n",
    "    \n",
    "    hem_url = imagesoup.find('img', class_=\"wide-image\")['src']\n",
    "    \n",
    "    img_url = (base_url and hem_url)\n",
    "\n",
    "    img_title = browser.find_by_css('.title').text\n",
    "    \n",
    "    hemisphere_image_data.append({\"title\": img_title,\n",
    "                              \"img_url\": img_url})\n",
    "    \n",
    "    browser.back()\n",
    "      \n",
    "browser.quit()\n",
    "\n",
    "hemisphere_image_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5260ace7",
   "metadata": {},
   "source": [
    "Items from each step: \n",
    "news_title\n",
    "news_p\n",
    "\n",
    "featured_image_url\n",
    "\n",
    "mars_html_table\n",
    "\n",
    "hemisphere_image_data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
