#scraping genre data from the wiki on music genre types
from requests.api import request
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import pickle

#I will scrape genre info from every link on the wiki music styles page
def get_genres():
    url = "https://en.wikipedia.org/wiki/List_of_music_styles"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    #working my way down the tree to the urls
    # uls = soup.find_all('ul')
    # print(uls)

    divs = soup.find_all('div', class_ ='div-col')#this ensures its just the list of genres
    uls = [div.ul for div in divs]#getting all the uls
    lis = [ul.find_all('li') for ul in uls]

    #flattening the list
    lis = [item for sublist in lis for item in sublist]

    links = []
    titles = []
    #retrieving the links and the titles
    for li in lis:
        try:
            link = li.a.get('href')
            links.append(link)

            title = li.a.get('title')
            titles.append(title)
        except:
            links.append('error')
            titles.append('error')


    #checking which genres have duplicated titles
    # for title in titles:
    #     print(f'{title} has counts {titles.count(title)}')

    #check proved what I though some genres are listed multiple times within the wiki since they fit 
    # within more than one class (i.e. african music)


    #creating a dictionary that will contain the genre information to start
    genres = {title: {'link': link} for title, link in zip(titles, links)}
    return genres

#begin work on scrapping information about each genre
def get_genre_info(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    #looking to get the paragraph description from the website
    div = soup.find('div', class_ = 'mw-parser-output')
    description = div.p.get_text()

    return description

# genres = get_genres()
# for genre in tqdm(genres):
#     try:
#         genres[genre]['description'] = get_genre_info(("https://en.wikipedia.org" + genres[genre]['link']))
#     except:
#         print(genre)

#let's save the scraped data into a pickled file so we don't have to constantly scrape data
# f = open('genres_dict.pkl', 'wb')
# pickle.dump(genres, f)
# f.close()

#getting artist information
with open('genres_dict.pkl', 'rb') as f:
    genres = pickle.load(f)

#we need to loop through all the links again to find the artists that are mentioned in the genre and their websites
# def get_artist(url):
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html5lib')

#     divs = soup.find_all('div', id = 'mw-pages')
#     return divs


def get_artist(url, genre):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')




test_url = "https://en.wikipedia.org/wiki/Alternative_R%26B"

print(get_artist(test_url, 'Alternative R&B'))