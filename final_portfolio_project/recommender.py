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

with open('choice_dict_nodes.pkl', 'rb') as f:
    choice_nodes = pickle.load(f)
f.close()

# the main function will the wrapper function that displays the in line information and should be callable incase of repeats
def main():
    print("""Welcome to the music recommender. We will narrow down a recommendation by genre.""")
    narrow = None
    while not narrow:
        narrow = input("To look at list of all genres type \"all\". If you would like to look at the genres under a specific letter type the letter: ").lower()

        if narrow == 'all': #will print all of the genres in the list
            for idx, choice in enumerate(choice_nodes):
                print(idx, choice_nodes[choice].info)
        elif narrow in choice_nodes.keys():
            for idx, genre in enumerate(choice_nodes[narrow].info):
                print(idx, genre) 
            narrow = int(input('Enter the corresponding number from the list above to find out more about the genre.'))
        else:
            print('Oops, wrong input, try again')
            narrow = None


main()

