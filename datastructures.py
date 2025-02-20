class DisjointUnionSets:
    # idea: have a list of n elements where n is the number of vertices in the graph
    # the value at each index i indicates which set vertx i belongs to
    # thus, each vertex can only belong to one set and initially each is its own set
    def __init__ (self, n):
       # create a collection of n disjoint sets where n = number of vertices in graph
       self.collection = list(range(n))
       self.len = n

    def find(self, v):
       # find set containing vertex v and return name
       return self.collection[v]
    
    def union(self, u, v):
       # merge set containing u and set containing v
       u_set = self.find(u)
       v_set = self.find(v)
       # if the sets are the same, just return that one
       if u_set == v_set:
          return u_set
       # if they are disjoint, merge
       for i in range(self.len):
            if self.collection[i] == v_set:
               self.collection[i] = u_set

def betina_heap(diction):
  min_val = list(diction.values())[0]
  min_index = 0
  for i in range(len(diction)):
    if list(diction.values())[i] < min_val:
      min_val = list(diction.values())[i]
      min_index = i
  return list(diction.keys())[min_index], min_index