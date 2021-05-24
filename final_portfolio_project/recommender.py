"""
This project will take user input to create music recommendations for them based on a genre or year. 
"""
import pickle
with open('genres_dict.pkl', 'rb') as f:
    genres = pickle.load(f)

print(genres)