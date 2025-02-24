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

# Complete graphs on n vertices, where the vertices are points chosen uniformly 
# at random inside the unit cube (3 dimensions) and hypercube (4 dimensions).
# As with the unit square case above, the weight of an edge is 
# just the Euclidean distance between its endpoints.
def graph_cube3(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    for i in range(n):
        x1 = np.random.uniform(0, 1)
        y1 = np.random.uniform(0, 1)
        z1 = np.random.uniform(0, 1)
        for j in range(i, n):
            if i != j:
                x2 = np.random.uniform(0, 1)
                y2 = np.random.uniform(0, 1)
                z2 = np.random.uniform(0, 1)
                dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                weight[(i,j)] = dist
                weight[(j,i)] = dist
            else:
                graph[i][j] = 0
    return graph, weight

def graph_cube4(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    for i in range(n):
        w1 = random.uniform(0,1)
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        z1 = random.uniform(0, 1)
        for j in range(i, n):
            if i != j:
                w2 = random.uniform(0, 1)
                x2 = random.uniform(0, 1)
                y2 = random.uniform(0, 1)
                z2 = random.uniform(0, 1)
                dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                weight[(i,j)] = dist
                weight[(j,i)] = dist
            else:
                graph[i][j] = 0
    return graph, weight