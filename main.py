import urllib.request
import bs4 

''' 
Beautiful Soup traverses HTML text through Python to allow scraping off web pages 

'''

# create a web client 
from urllib.request import urlopen as uReq  # import the library to open web urls through python
import urllib
from bs4 import BeautifulSoup as soup 

# parsing the newegg graphics card search site 
my_url= "https://www.newegg.com/p/pl?d=graphics+card"   # url of webpage for scraping

headers= {'User-Agent': 'Mozilla/5.0'}

# make the first request to open the webpage 
req= urllib.request.Request(my_url, headers=headers)

# open up the website for processing using uReq function 
uClient= uReq(req)    # open the connection to grab the webpage and download the webpage as HTML 

page_html= uClient.read()  # read once of everything that's downloaded (will be discarded afterwards)

uClient.close()     # close the internet connection 

# html parsing
page_soup= soup(page_html, "html.parser")

body_tag= page_soup.find("body") # find the body content 
inner_div= body_tag.find("div", id= "app")
page_div= inner_div.find("div", class_= "page-content")
containers= page_div.find_all("div", class_="item-cell")


# find the price of the items in the current webpage
item=containers[0]
print(item.find("li", class_= "price-current"))