import numpy as np

class DisjointUnionSets:
   def __init__ (self, n):
      self.rank = np.zeros(n)
      self.parent = np.arange(0,n)
   
   def find(self, x):
      p = self.parent[x]
      if p == x:
         return x
      else:
         return self.find(p)
   
   def link(self, x, y):
      rank_x = self.rank[x]
      rank_y = self.rank[y]
      if rank_x > rank_y:
         x, y = y, x
      if rank_x == rank_y:
         self.rank[y] += 1
      self.parent[x] = y
   
   def union(self, x, y):
      self.link(self.find(x), self.find(y))


def betina_heap(diction):
  min_val = list(diction.values())[0]
  min_index = 0
  for i in range(len(diction)):
    if list(diction.values())[i] < min_val:
      min_val = list(diction.values())[i]
      min_index = i
  return list(diction.keys())[min_index], min_index