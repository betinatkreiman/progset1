import numpy as np
import sys
import datastructures as ds
import graphs as g

# input to command line: progset.py 0 numpoints numtrials dimension
program_name, flag, numpoints, numtrials, dimension = sys.argv
# output: average numpoints numtrials dimension

def prims(g, w, s):
  d = np.full(len(g), 1000000000)
  S = {}
  H = []
  prev = {s: None}
  d[s] = 0
  H = {s:0}

  while H != []:
    min_val, _ = ds.betina_heap(H)

    u = (min_val, H.pop(min_val))
    S[u[0]] = u[1]

    for i in range(len(g[u[0]])):
      if g[u[0]][i] == 1:
        u_val = int(u[0])
        v_val = int(g[u[0]][i])

        if d[v_val] > w[(u_val, v_val)]:
          d[v_val] = w[(u_val, v_val)]
          prev[v_val] = u_val
          H[v_val] = w[(u_val, v_val)]
    return d, prev

def kruskals(g,w):
  # w = dictionary
  # g = adj. matrix
  X = set()
  # create set for each vertex; assuming vertices are numbered 0 to n-1
  vertex_count = len(g)
  dus = ds.DisjointUnionSets(vertex_count)
  # sort edges by weight
  sort_w = {k: v for k, v in sorted(w.items(), key=lambda item: item[1])}
  for (i,j) in sort_w:
    if dus.find(i) != dus.find(j):
      X.add((i,j))
      dus.unionSets(i,j)
  return X

import time

def run(alg, type_graph, ns, numb_times):
  times = []

  for n in ns:
    current_time = 0
    for _ in range(numb_times):

      g, w = type_graph(n)

      start = time.time()
      alg(g, w, 0)
      end = time.time()

      current_time += end - start

    current_time /= numb_times
    times.append(current_time)

  return times

