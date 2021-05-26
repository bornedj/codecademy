import pickle
#def the class for tree node
class TreeNode:
  def __init__(self, name, info):
    self.name = name # data
    self.info = info
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children


#loading in the necessary objects
with open('artists_by_genre.pkl', 'rb') as f:
  artists_by_genre = pickle.load(f)
f.close()

#artist info
with open('artists_info.pkl', 'rb') as f:
  artist_info = pickle.load(f)
f.close()

# print(artist_info)
# print(artists_by_genre)

# set up a function to iterate through the list of all the artists by genre 
# and check if they have artists in them to be added as children.
# also create the tree nodes for the artists 