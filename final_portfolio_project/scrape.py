#scraping genre data from the wiki on music genre types
from os import link
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

f.close()

#we need to loop through all the links again to find the artists that are mentioned in the genre and their websites
def get_artist():
    url = "https://en.wikipedia.org/wiki/Category:Lists_of_musicians_by_genre"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    divs = soup.find_all('div', class_ = 'mw-category-group')
    uls = [div.ul for div in divs]
    lis = [ul.find_all('li') for ul in uls]

    #flattening the list
    lis = [item for sublist in lis for item in sublist]

    links = [li.a.get('href') for li in lis]
    titles = [li.a.get('title') for li in lis]
    
    list_of_artist_by_genre = {title: {'link_list': link} for title, link in zip(titles, links)}#dictionary contains the list of as key and then the link
        
    return list_of_artist_by_genre


def get_artist_links(url):
    #setup bs4
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    #get list of artist links
    try:
        divs = soup.find_all('div', class_ ='div-col')#this ensures its just the list of genres
        uls = [div.ul for div in divs]#getting all the uls
        lis = [ul.find_all('li') for ul in uls]

        #flattening the list
        lis = [item for sublist in lis for item in sublist]
    except:
        return None

    links = []
    artists =[]
    for li in lis:    
        try:
            link = li.a.get('href')
            links.append(link)

            title = li.a.get('title')
            artists.append(title)
        except:
            links.append(None)
            artists.append(None)

    artists_and_links = {artist: link for artist, link in zip(artists, links)}
    return artists_and_links


# link_dict = get_artist()
# for genre in tqdm(link_dict):
#     link_dict[genre]["artist_dict"] = get_artist_links("https://en.wikipedia.org" + link_dict[genre]['link_list'])

#writting the file so that I don't need to scrape again
# f = open('artists_by_genre.pkl', 'wb')
# pickle.dump(lists_of_artists, f)
# f.close()

#reading back in the dictionary with tons of info on artists
with open('artists_by_genre.pkl', 'rb') as f:
    lists_of_artists = pickle.load(f)
f.close()

#cleaning the dictionary
# copy = lists_of_artists.copy()
# for list in copy:
#     if lists_of_artists[list]['artist_dict'] == None:
#         lists_of_artists.pop(list)


def get_artist_info(url):
    pass

#looping through the dictionary to create the artist dictionary
for list in lists_of_artists:
    for key in lists_of_artists[list]['artist_dict']:
        url = "https://en.wikipedia.org" + lists_of_artists[list]['artist_dict'][key]

