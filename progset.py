# graph is adjacency matrix
# weights is dictionary
# s is just node number aka int

import numpy as np

def prims(g, w, s):
  d = np.full(len(g), 1000000000)
  S = []
  H = []
  prev = {s: None}
  d[s] = 0
  H.append((s,0))

  while H != []:
    u = 0
  return -1

def kruskals(g,w):
  '''
  # w = dictionary
  # g = adj. matrix
  X = emptyset()
  # create set for each vertex; assuming vertices are numbered 0 to n-1
  vertex_count = len(g)
  for i in range(vertex_count):
    makeset(i)
  # sort edges by weight
  sort_w = {k: v for k, v in sorted(w.items(), key=lambda item: item[1])}
  for (i,j) in sort_w:
    if !(find(i)==find(j)):
      X = ...
      union(i,j)
  return X
  '''
  return -1