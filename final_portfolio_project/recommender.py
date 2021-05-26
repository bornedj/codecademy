"""
This project will take user input to create music recommendations for them based on a genre or year. 
"""
import pickle
from treenode import TreeNode

with open('genre_node_dict.pkl', 'rb') as f:
    genre_nodes = pickle.load(f)
f.close()

with open('artist_node_dict.pkl', 'rb') as f:
    artist_nodes = pickle.load(f)
f.close()


# the main function will the wrapper function that displays the in line information and should be callable incase of repeats
def main():
    pass


        



