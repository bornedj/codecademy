"""
This project will take user input to create music recommendations for them based on a genre or year. 
"""
import pickle
from treenode import TreeNode

with open('genres_dict.pkl', 'rb') as f:
    genres = pickle.load(f)

#creating tree nodes for all the genres
all_genre_nodes = [TreeNode(title, genres[title]) for title in genres]
for node in all_genre_nodes:
    print(node.info)