#scraping genre data from the wiki on music genre types
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import pickle
import re
from treenode import TreeNode

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
# with open('genres_dict.pkl', 'rb') as f:
#     genres = pickle.load(f)
# f.close()

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
# with open('artists_by_genre.pkl', 'rb') as f:
#     lists_of_artists = pickle.load(f)
# f.close()

#cleaning the dictionary
# copy = lists_of_artists.copy()
# for list in copy:
#     if lists_of_artists[list]['artist_dict'] == None:
#         lists_of_artists.pop(list)


def get_artist_info(url):
    #setup the soup
    # url = "https://en.wikipedia.org/wiki/T-Pain"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    # all_i = soup.find_all('i')
    # all_a = [i.a for i in all_i]

    
    a_tags = soup.find_all('a', title = re.compile('album'))
    albums = [tag.get('title') for tag in a_tags]
    return albums

#looping through the dictionary to create the artist dictionary
"""
artists_info = {}
for list in tqdm(lists_of_artists):
    for key in tqdm(lists_of_artists[list]['artist_dict']):
        if lists_of_artists[list]['artist_dict'][key]:
            url = "https://en.wikipedia.org" + lists_of_artists[list]['artist_dict'][key]
            
            try:
                artists_info[key] = get_artist_info(url)
            except:
                artists_info[key] = "error"
"""
# print(artists_info)

#save the artists_info data
# f = open('artists_info.pkl', 'wb')
# pickle.dump(artists_info, f)
# f.close()

#----------------------------------------------------------------------------------------------------------------------------------------
#cleaning out the (album) from each alubm in an artists list
# for artist in artist_info:
#   if artist_info[artist]:#check if the artist has a list of albums
#     #if they do use regex to replace values
#     for i in range(len(artist_info[artist])):
#       corrected_album = artist_info[artist][i]
#       corrected_album = corrected_album[:corrected_album.find('(') - 1]
#       artist_info[artist][i] = corrected_album


#re-writting the file now that it's corrected
# f = open('artists_info.pkl', 'wb')
# pickle.dump(artist_info, f)
# f.close()

# print(artist_info)


# set up a function to iterate through the list of all the artists by genre 
# and check if they have artists in them to be added as children.



#---------------------------------------------------------------------------------------------------------------------------------------
#from the recommender script, reads in pickled objects and creates the dictionaries for genres and artists nodes

with open('genres_dict.pkl', 'rb') as f:
    genres = pickle.load(f)
f.close()

with open('artists_info.pkl', 'rb') as f:
    artists = pickle.load(f)
f.close()

with open('artists_by_genre.pkl', 'rb') as f:
    artist_genre = pickle.load(f)
f.close()


#creating tree nodes for all the genres
all_genre_nodes = {genre: TreeNode(genre, artists) for genre, artists in genres.items()}

#creating the tree nodes for each artist
all_artist_nodes = {artist: TreeNode(artist, albums) for artist, albums in artists.items()}

#assigning genres the right children
for genre in genres: #looping through the genre list
    # print(genre)
    for list in artist_genre: #looping through the dict that contains the artists within their respective 
        if genre.lower() in list.lower(): #checking if the list contains the genre name
            # artist_list = list(artist_genre[list]['artist_dict'].keys()) #get a list of the artists within the genre to loop through
            if artist_genre[list]['artist_dict']: #checks if there artists listed in the genre
                for key in artist_genre[list]['artist_dict'].keys(): #loops through the artists within that genre
                    current_parent = all_genre_nodes[genre] #get the current genre node
                    try:
                        current_parent.add_child(all_artist_nodes[key]) #add the artist as a child to the current child node
                    except:
                        print('error', key)

#writing the dictionary that contains all of the tree nodes on genres
f = open('genre_node_dict.pkl', 'wb')
pickle.dump(all_genre_nodes, f)
f.close()

#writting the dictionary that contains all the artists nodes into a pickled file
f = open('artist_node_dict', 'wb')
pickle.dump(all_artist_nodes,f)
f.close()