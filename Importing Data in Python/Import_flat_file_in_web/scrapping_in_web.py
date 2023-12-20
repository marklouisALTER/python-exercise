from bs4 import BeautifulSoup
import requests

# specify the url
url = 'https://www.python.org/~guido/'

# get the requests
r = requests.get(url)

# turn it into text
html_doc = r.text

# create an beaufitul soup object from the text
soup = BeautifulSoup(html_doc)

# pretiffy the soup object
# pretty_soup = soup.prettify()

# print the pretty soup
# print(pretty_soup)

# get the title 
# print(soup.title)

# get all the links in the web
# a_tag = soup.find_all('a')

# for link in a_tag:
#     print(link.get('href'))	

# get all the text
# get_text = soup.get_text()
# print(get_text)





