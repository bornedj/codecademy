#scraping genre data from the wiki on music genre types
from bs4 import BeautifulSoup
import requests

#I will scrape genre info from every link on the wiki music styles page

url = "https://en.wikipedia.org/wiki/List_of_music_styles"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

li_s = soup.find_all('li', 'href')
print(li_s)