import random
import numpy as np
import math

def graph_basic(n):
    # input: int n (number of vertices)
    # output: adj. matrix of complete graph, 
    #         dict of weights, chosen uniformly at random in [0,1]
    graph = np.ones((n, n))
    weight = {}
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        graph[v][v] = 0
        for edge in range(v, n):
            w = random.uniform(0, 1)
            weight[(v,edge)] = w
            weight[(edge,v)] = w
    return graph, weight

# "Hypercube” graphs on n vertices, where (a, b) is an edge iff |a − b| = 2^i for some i,
# and the weight of each edge is a real number chosen uniformly at random on [0,1].
# (This does not exactly match the true definition of a hypercube graph,
# but it is the definition we will work with for simplicity)
def hypercube(n):
  graph = np.zeros((n, n))
  edges = {}

  for i in range(n):
    for j in range(n):
      if i != j:
      #print(abs(i - j))
        if math.log(abs(i - j), 2).is_integer():
          graph[i][j] = 1
          graph[j][i] = 1
          w = np.random.uniform(0, 1)
          edges[(i,j)] = w
          edges[(j,i)] = w

  return graph, edges

# Complete graphs on n vertices, where the vertices are points chosen uniformly at
# random inside the unit square. (That is, the points are (x,y), with x and y each
# a real number chosen uniformly at random from [0, 1].) The weight of an edge is
# just the Euclidean distance between its endpoints.
def uniformly(n):
  graph = np.ones((n, n))
  edges = {}

  for i in range(n):
    for j in range(n):
      if i != j:
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        w = np.sqrt((x - i)**2 + (y - j)**2)
        edges[(i,j)] = w
        edges[(j,i)] = w
    else: 
       graph[i][j] = 0

  return graph, edges

def graph_cube(n):
    # input: int n (number of vertices)
    # output: adj. matrix of complete graph, 
    #         adj. matrix of weights, chosen uniformly at random in [0,1]
    graph = 0
    weight = 0
    return graph, weight