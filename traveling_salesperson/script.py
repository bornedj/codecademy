import random
from random import randrange
from Graph import Graph
from Vertex import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)

def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

# Define your functions below:

#helper function to check if all vertices have been visited
def visited(visited_vertices):
  #i will keep track using a dictionary of keys with boolean values
  for vertex in visited_vertices:
    if not visited_vertices[vertex]:#if it hasn't been visited return false
      return False
  #after we have finished the loop return the answer    
  return True
#function to find the path for the sales person
def traveling_salesperson(graph):
  final_path = ""#contains the final path for the sales person

  visited_vertices = {key: False for key in graph.graph_dict}

  #selecting a random starting point
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertices[current_vertex] = True
  final_path += current_vertex

  #checking to see if we have visited all the points in the graph
  visited_all_check = visited(visited_vertices)

  while not visited_all_check:#loop while not all have been visited
    current_edges = graph.graph_dict[current_vertex].get_edges()#list of edges returned
    current_edge_weights = {}
    for edge in current_edges:
      current_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)

    #check to see if we have found our next vertex
    found_next_vertex = False
    next_vertex = ''#will contain key for next vertex
    
    #looping until we find the next vertex
    while not found_next_vertex:
      #if there are no edges break the loop, cant be next vertex
      if current_edge_weights == {}:
        break
      
      # print(current_edge_weights)
      next_vertex = min(current_edge_weights, key = current_edge_weights.get)
      
      #check to see if the next_Vertex has been visited
      if visited_vertices[next_vertex]: #boolean dict
        #if it's been visited remove from the dict
        current_edge_weights.pop(next_vertex)
      else:
        found_next_vertex = True

      #check to see if there are more edges to look at after the while loop
      if current_edge_weights is None:
        visited_all_check = True #break the outer while loop since we have checked all vertices
      else: #continue the loop with new vertex
        current_vertex = next_vertex
        visited_vertices[current_vertex] = True
        final_path += current_vertex
        visited_all_check = visited(visited_vertices)


  
  return final_path


#check to see if program is working
graph = build_tsp_graph(True)
print(traveling_salesperson(graph))

