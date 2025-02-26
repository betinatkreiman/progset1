import random
import numpy as np
import math
import time

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

def graph_basic_faster(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph with some edges cut, 
    #         dict of weights, chosen uniformly at random in [0,1]
    graph = np.ones((n, n))
    weight = {}
    # decide edges to ignore
    cut_off = float('inf')
    if n > 3:
        cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        graph[v][v] = 0
        for edge in range(v, n):
            w = random.uniform(0, 1)
            if w < cut_off:
                weight[(v,edge)] = w
                weight[(edge,v)] = w
            else:
                graph[v][edge] = 0
                graph[edge][v] = 0
    return graph, weight

def graph_basic_adj_list(n):
    # input: int n (number of vertices)
    # output: (sort of) adj. list of complete graph, 
    #         dict of weights, chosen uniformly at random in [0,1]
    graph_list = [[] for _ in range(n)]
    weight = {}
    # decide edges to ignore
    cut_off = float('inf')
    if n > 3:
        cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        for edge in range(v+1, n):
            w = random.uniform(0, 1)
            if w < cut_off:
                weight[(v,edge)] = w
                weight[(edge,v)] = w
                graph_list[v].append(edge)
                graph_list[edge].append(v)
    # convert to array with padding
    graph = np.zeros((n,n), dtype=int)
    for i in range(n):
        for j in range(n):
            l = len(graph_list[i])
            if j < l:
                graph[i][j] = graph_list[i][j]
            else:
                graph[i][j] = -1
    return graph, weight

# "Hypercube” graphs on n vertices, where (a, b) is an edge iff |a − b| = 2^i for some i,
# and the weight of each edge is a real number chosen uniformly at random on [0,1].
# (This does not exactly match the true definition of a hypercube graph,
# but it is the definition we will work with for simplicity)
def hypercube(n):
  graph = np.zeros((n, n))
  edges = {}

  for i in range(n):
    for j in range(i, n):
      if i != j:
      #print(abs(i - j))
        if math.log(abs(i - j), 2).is_integer():
          graph[i][j] = 1
          graph[j][i] = 1
          w = np.random.uniform(0, 1)
          edges[(i,j)] = w
          edges[(j,i)] = w

  return graph, edges

def hypercube_faster(n):
    graph = np.zeros((n, n))
    edges = {}
    cut_off = 0.45 + 1/(n**(1/4))
    for i in range(n):
        for j in range(i, n):
            if i != j:
            #print(abs(i - j))
                w = np.random.uniform(0, 1)
                if w < cut_off:
                    if math.log(abs(i - j), 2).is_integer():
                        graph[i][j] = 1
                        graph[j][i] = 1
                        edges[(i,j)] = w
                        edges[(j,i)] = w

    return graph, edges

# Complete graphs on n vertices, where the vertices are points chosen uniformly at
# random inside the unit square. (That is, the points are (x,y), with x and y each
# a real number chosen uniformly at random from [0, 1].) The weight of an edge is
# just the Euclidean distance between its endpoints.
def uniformly(n):
    graph = np.ones((n, n))
    weight = {}
    points = np.zeros((n,2))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        points[i] = x,y
    for i in range(n):
        (x1,y1) = points[i]
        for j in range(i, n):
            if i != j:
                x2,y2 = points[j]
                dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
                weight[(i,j)] = dist
                weight[(j,i)] = dist
            else:
                graph[i][j] = 0
    return graph, weight

def uniformly_faster(n):
    graph = np.zeros((n, n))
    weight = {}
    points = np.zeros((n,2))
    # remove large edges
    cut_off = 3/(2**math.log(n,4))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        points[i] = x,y
    for i in range(n):
        (x1,y1) = points[i]
        for j in range(i, n):
            if i != j:
                x2,y2 = points[j]
                dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
                if dist < cut_off:
                    weight[(i,j)] = dist
                    weight[(j,i)] = dist
                    graph[i][j] = 1
                    graph[j][i] = 1
    return graph, weight

# Complete graphs on n vertices, where the vertices are points chosen uniformly 
# at random inside the unit cube (3 dimensions) and hypercube (4 dimensions).
# As with the unit square case above, the weight of an edge is 
# just the Euclidean distance between its endpoints.
def graph_cube3(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    points = np.zeros((n,3))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (x,y,z)
    for i in range(n):
        (x1,y1,z1) = points[i]
        for j in range(i, n):
            if i != j:
                (x2,y2,z2) = points[j]
                dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                weight[(i,j)] = dist
                weight[(j,i)] = dist
            else:
                graph[i][j] = 0
    return graph, weight
                                
def graph_cube3_faster(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    points = np.zeros((n,3))
    # decide edges to delete
    cut_off = 2.2/(2**(math.log(n,8)))
    # np.sqrt(3)/math.log(n,5)
    #3/(2**(math.log(n,4)))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (x,y,z)
    for i in range(n):
        (x1,y1,z1) = points[i]
        for j in range(i, n):
            if i != j:
                (x2,y2,z2) = points[j]
                dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                if dist < cut_off:
                    weight[(i,j)] = dist
                    weight[(j,i)] = dist
                else:
                    graph[i][j] = 0
                    graph[j][i] = 0
            else:
                graph[i][j] = 0
    return graph, weight

def graph_cube4(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    points = np.zeros((n,4))
    for i in range(n):
        w = np.random.uniform(0, 1)
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (w,x,y,z)
    for i in range(n):
        (w1,x1,y1,z1) = points[i]
        for j in range(i, n):
            if i != j:
                (w2,x2,y2,z2) = points[j]
                dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                weight[(i,j)] = dist
                weight[(j,i)] = dist
            else:
                graph[i][j] = 0
    return graph, weight

def graph_cube4_faster(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = np.ones((n, n))
    weight = {}
    points = np.zeros((n,4))
    cut_off = 2/(2**(math.log(n,16)))
    # np.sqrt(4)/(math.log(n, 5))
    for i in range(n):
        w = np.random.uniform(0, 1)
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (w,x,y,z)
    for i in range(n):
        (w1,x1,y1,z1) = points[i]
        for j in range(i, n):
            if i != j:
                (w2,x2,y2,z2) = points[j]
                dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
                if dist < cut_off:
                    weight[(i,j)] = dist
                    weight[(j,i)] = dist
                else:
                    graph[i][j] = 0
                    graph[j][i] = 0
            else:
                graph[i][j] = 0
    return graph, weight