from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 


class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for item in range(self.array_size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  #compressor
  def compress(self, hash_code):
    return hash_code % self.array_size

  #assign method
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]

    for lst in list_at_array:
      if lst[0] == key:
        lst[1] = value
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None

blossom = HashMap(len(flower_definitions))

for item in flower_definitions:
  blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))