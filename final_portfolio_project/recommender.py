"""
This project will take user input to create music recommendations for them based on a genre or year. 
"""
import pickle
from treenode import TreeNode

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
                    current_parent.add_child(all_artist_nodes[key]) #add the artist as a child to the current child node



        



