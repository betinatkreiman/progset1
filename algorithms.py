import datastructures as ds
import numpy as np
import graphs as gs

def prims_adj_list(g, w, s):
  n = len(g)
  d = np.full(n, float('inf'))
  S = {}
  #H = vertices to explore
  H = ds.Heap()
  H.init(0)

  prev = {s: None}
  d[s] = 0
  H.insert(s, 0)

  # make adj list from matrix
  graph = np.full((n,n), -1)
  for i in range(n):
      index = 0
      for j in range(n):
          edge = g[i][j]
          if edge == 1:
             graph[i][index] = j
             index += 1

  while H.heap != []:
    # extract min vertex in H
    min_node, min_weight = H.extractmin()

    # add min vertex to S
    S[min_node] = min_weight
    # loop over edges of min vertex
    for i in range(n):
      if graph[min_node][i] == -1:
          break
      else:
          v_val = graph[min_node][i]
          if v_val not in S:
            u_val = min_node
            w_uv = w[(u_val, v_val)]
            
            if d[v_val] > w_uv:
              d[v_val] = w_uv
              prev[v_val] = u_val
              H.insert(v_val, w_uv)

  mst_weight = 0
  max = 0
  for v in d:
    if v > max: max = v
    mst_weight += v
  return d, prev, mst_weight, max

def kruskals(g,w, nill):
  # nill = useless variable, so matches input/output of prim
  # w = dictionary
  # g = adj. matrix
  X = set()
  mstweight = 0
  # create set for each vertex; assuming vertices are numbered 0 to n-1
  vertex_count = len(g)
  dus = ds.DisjointUnionSets(vertex_count)
  # sort edges by weight
  sort_w = {k: v for k, v in sorted(w.items(), key=lambda item: item[1])}
  # (i,j) = (j,i) so we don't have to check both
  count = 0
  for (i,j) in sort_w:
    if count == 1:
       count == 0
       continue
    else: 
      count == 1
      if dus.find(i) != dus.find(j):
        X.add((i,j))
        dus.union(i,j)
        mstweight += sort_w[(i,j)]
        last_edge = (i,j)
  return nill, X, mstweight, sort_w[last_edge]

def prims_al(g, w, s):
  n = len(g)
  d = np.full(n, float('inf'))
  S = {}
  #H = vertices to explore
  H = ds.Heap()
  H.init(0)

  prev = {s: None}
  d[s] = 0
  H.insert(s, 0)

  while H.heap != []:
    # extract min vertex in H
    min_node, min_weight = H.extractmin()

    # add min vertex to S
    S[min_node] = min_weight
    # loop over edges of min vertex
    edge_list = g[min_node]
    for edge in edge_list:
        if edge not in S:
          a = min_node
          b = edge
          if edge < min_node:
            a = edge
            b = min_node
          w_uv = w[(a, b)]
          if d[edge] > w_uv:
            d[edge] = w_uv
            prev[edge] = min_node
            H.insert(edge, w_uv)

  mst_weight = 0
  max = 0
  for v in d:
    if v > max: max = v
    mst_weight += v
  return d, prev, mst_weight, max

def kruskals_al(g,w, nill):
  # nill = useless variable, so matches input/output of prim
  # w = dictionary
  # g = adj. list
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
  return nill, X, mstweight, sort_w[last_edge]
