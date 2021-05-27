#def the class for tree node
class TreeNode:
  def __init__(self, name, info):
    self.name = name # data
    self.info = info
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.name)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.name + " from " + self.name)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

  def dfs(root, target, path=()):
    path = path + (root,)

    if root.name == target:
      return path

    for child in root.children:
      path_found = dfs(child, target, path)

      if path_found is not None:
        return path_found

    return None
