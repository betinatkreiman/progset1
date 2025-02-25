import datastructures as ds
import numpy as np
import graphs as gs

def prims(g, w, s):
  d = np.full(len(g), 1000000000)
  S = {}
  H = {}
  prev = {s: None}
  d[s] = 0
  H = {s:0}

  while H != {}:
    #print(H)
    min_val, min_index = ds.betina_heap(H)

    u = (min_val, H.pop(min_val))

    #print(u)
    S[u[0]] = u[1]

    for i in range(len(g[u[0]])):
      #print("HELLO", g[u[0]])
      if g[u[0]][i] == 1:
        u_val = int(u[0])
        #print("maybe v val", g[u[0]])
        #v_val = int(g[u[0]][i])
        v_val = i

        if d[v_val] > w[(u_val, v_val)]:
          d[v_val] = w[(u_val, v_val)]
          prev[v_val] = u_val
          H[v_val] = w[(u_val, v_val)]
  mst_weight = 0
  max = 0
  for v in S.values():
    if v > max: max = v
    mst_weight += v
  return d, prev, mst_weight, max

def kruskals(g,w):
  # w = dictionary
  # g = adj. matrix
  X = set()
  mstweight = 0
  # create set for each vertex; assuming vertices are numbered 0 to n-1
  vertex_count = len(g)
  dus = ds.DisjointUnionSets(vertex_count)
  # sort edges by weight
  sort_w = {k: v for k, v in sorted(w.items(), key=lambda item: item[1])}
  for (i,j) in sort_w:
    if dus.find(i) != dus.find(j):
      X.add((i,j))
      dus.union(i,j)
      mstweight += sort_w[(i,j)]
      last_edge = (i,j)
  return X, mstweight, sort_w[last_edge]
