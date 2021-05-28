"""
This project will take user input to create music recommendations for them based on a genre or year. 
"""
import pickle
from treenode import TreeNode
import sys

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
    print("""\n\nWelcome to the music recommender. We will narrow down a recommendation by genre.""")
    narrow = None
    while not narrow:
        narrow = input("To look at list of all genres type \"all\". If you would like to look at the genres under a specific letter type the letter: ").lower()

        #narrowing down after displaying all the genres
        if narrow == 'all': #will print all of the genres in the list
            for idx, choice in enumerate(choice_nodes):
                print(idx, choice_nodes[choice].info, '\n')
            
            #get user input to narrow down to letter
            narrow = int(input("Enter the corresponding number with the list of genres you would like to learn more about: "))
            #loops until user has submitted a valid number
            while narrow not in range(len(choice_nodes.keys())):
                for idx, choice in enumerate(choice_nodes):#print the options again
                    print(idx, choice_nodes[choice].info, '\n')
                narrow = int(input('Please pick a number corresponding the genre lists printed above. The number should be between 0-25: '))

            #show the genres based on the number the selected
            for i, key in enumerate(choice_nodes): 
                if i == narrow:
                    selected_choice = key#saving the letter from choices
                    for j, genre in enumerate(choice_nodes[key].info):#displaying genres and numbers to select with
                        print(j, genre)
                    
                    #saving the selection
                    narrow = int(input('Please select the genre based on the number to it\'s left: '))
                    for k, genre in enumerate(choice_nodes[key].info):
                        if k == narrow:
                            selected_genre = choice_nodes[key].info[k] #saving the genre to display

            
            #show the genre description
            print("\nHere is the description of the genre as defined by wikipedia:\n")
            for child in choice_nodes[selected_choice].children:
                if child.name == selected_genre:
                    current_node = child
                    print(current_node.info['description'])

            #check if the user wants to see the available artists
            narrow = input("\n\nWould you like to see some artists from this genre (if wiki lists them) type y/n: ").lower()
            if narrow == 'y':

                #look for the artists within the current_node
                if current_node.children:
                    for idx, child in enumerate(current_node.children):
                        print(idx, child.name)
                    narrow = int(input("\nSelect a band by the number to it's left based on the list above: "))
                    for idx, child in enumerate(current_node.children):
                        if narrow == idx:
                            current_node = current_node.children[idx]

                    #show the information about the artists
                    print("\nHere is the artists description and records:\n")
                    print(current_node.name)
                    if current_node.info:
                        for album in current_node.info:
                            print(album)
                    else:
                        print('They don\'t have listed albums on wikipidea')

                    narrow = input("\n\nWould you like to look for another genre? Type y if yes and anything else to quit.").lower()
                    if narrow == 'y':
                        main()
                    else:#they don't exit the program
                        sys.exit()

                    
            else: #they don't want to see artists, check if they want to see another genre
                narrow = input("\n\nWould you like to look for another genre? Type y if yes and anything else to quit.").lower()
                if narrow == 'y':
                    main()
                else:#they don't exit the program
                    sys.exit()
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        #selected by letter/number beforehand
        elif narrow in choice_nodes.keys():
            key = narrow
            for idx, genre in enumerate(choice_nodes[narrow].info):
                print(idx, genre) 


            narrow = int(input('Enter the corresponding number from the list above to find out more about the genre: '))
            for k, genre in enumerate(choice_nodes[key].info):
                if k == narrow:
                    selected_genre = choice_nodes[key].info[k] #saving the genre to display

            #show the genre description
            print("Here is the description of the genre as defined by wikipedia:\n")
            for child in choice_nodes[key].children:
                if child.name == selected_genre:
                    current_node = child
                    print(current_node.info['description'])

            #check if the user wants to see the available artists
            narrow = input("Would you like to see some artists from this genre (if wiki lists them) type y/n: ").lower()
            if narrow == 'y':

                #look for the artists within the current_node
                if current_node.children:
                    for idx, child in enumerate(current_node.children):
                        print(idx, child.name)
                    narrow = int(input("\nSelect a band by the number to it's left based on the list above: "))
                    for idx, child in enumerate(current_node.children):
                        if narrow == idx:
                            current_node = current_node.children[idx]

                    #show the information about the artists
                    print("\nHere is the artists description and records:\n")
                    print(current_node.name)
                    if current_node.info:
                        for album in current_node.info:
                            print(album)
                    else:
                        print('They don\'t have listed albums on wikipidea')

                    narrow = input("\n\nWould you like to look for another genre? Type y if yes and anything else to quit.").lower()
                    if narrow == 'y':
                        main()
                    else:#they don't exit the program
                        sys.exit()
                
                else: #wiki didn't list any bands
                    print("\nWikipedia does not have any bands listed for this genre.")
                    narrow = input("\n\nWould you like to look for another genre? Type y if yes and anything else to quit.").lower()
                    if narrow == 'y':
                        main()
                    else:#they don't exit the program
                        sys.exit()


            else: #they don't want to see artists, check if they want to see another genre
                narrow = input("Would you like to look for another genre? Type y if yes and anything else to quit.").lower()
                if narrow == 'y':
                    main()
                else:#they don't exit the program
                    sys.exit()

        else:
            print('Oops, wrong input, try again')
            narrow = None


main()

# for key in genre_nodes:
#     if genre_nodes[key].children:
#         print(key)