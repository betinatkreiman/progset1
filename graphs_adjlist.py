import random
import numpy as np
import math
import time

def graph_basic_al(n):
    # input: int n (number of vertices)
    # output: adj. list of graph with some edges cut, 
    #         dict of weights, chosen uniformly at random in [0,1]
    graph = [[] for _ in range(n)]
    weight = {}
    # decide edges to ignore
    cut_off = float('inf')
    if n > 3:
        cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        for edge in range(v+1,n):
            w = random.uniform(0, 1)
            if w < cut_off:
                weight[(v,edge)] = w
                graph[v].append(edge)
                graph[edge].append(v)
    return graph, weight

def hypercube_al(n):
    graph = [[] for _ in range(n)]
    edges = {}
    cut_off = 0.45 + 1/(n**(1/4))
    for i in range(n):
        for j in range(i+1,n):
                if i != j:
            #print(abs(i - j))
                    w = np.random.uniform(0, 1)
                    if w < cut_off:
                        if math.log(abs(i - j), 2).is_integer():
                            edges[(i,j)] = w
                            graph[i].append(j)
                            graph[j].append(i)
    return graph, edges

def uniformly_al(n):
    graph = [[]for _ in range(n)]
    weight = {}
    points = np.zeros((n,2))
    # remove large edges
    cut_off = 3/(n**(1/2))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        points[i] = x,y
    for i in range(n):
        (x1,y1) = points[i]
        for j in range(i+1, n):
            x2,y2 = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
            if dist < cut_off:
                weight[(i,j)] = dist
                graph[i].append(j)
                graph[j].append(i)
    return graph, weight
                                
def graph_cube3_al(n):
    # input: int n (number of vertices)
    # output: adj. list of graph, dict of weights
    graph = [[] for _ in range(n)]
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
        for j in range(i+1,n):
            (x2,y2,z2) = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                weight[(i,j)] = dist
                graph[i].append(j)
                graph[j].append(i)
    return graph, weight

def graph_cube4_al(n):
    # input: int n (number of vertices)
    # output: adj. list of graph, dict of weights
    graph = [[] for _ in range(n)]
    weight = {}
    points = np.zeros((n,4))
    cut_off = 1.7/(n**(1/4))
    # save points
    for i in range(n):
        w = np.random.uniform(0, 1)
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (w,x,y,z)
    # make graph
    for i in range(n):
        (w1,x1,y1,z1) = points[i]
        for j in range(i+1, n):
            (w2,x2,y2,z2) = points[j]
            dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                weight[(i,j)] = dist
                graph[i].append(j)
                graph[j].append(i)
    return graph, weight

def graph_basic_stat(n):
    graph = [[] for _ in range(n)]
    weight = {}
    cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # pick expected number of edges
    if cut_off > 1:
        cut_off = 1
    edge_total = (n)*(n-1)*0.5
    k = math.ceil((cut_off)*edge_total)
    for j in range(k):
        # pick random edges, assume ordered least to greatest
        source = random.randint(0, n-1)
        target = random.randint(0, n-1)
        while (target in graph[source] or target == source):
            source = random.randint(0, n-1)
            target = random.randint(0, n-1)
        graph[source].append(target)
        graph[target].append(source)
        # jth order stat
        w = np.random.beta(j+1, edge_total - j + 2)
        a = min(source, target)
        b = max(source, target)
        weight[(a, b)] = w
    return graph, weight

def graph_basic_no_w(n):
    # input: int n (number of vertices)
    # output: adj. list of graph with some edges cut, 
    #         edges as tuple (target, weight)
    #         weight chosen uniformly at random in [0,1]
    graph = [[] for _ in range(n)]
    # decide edges to ignore
    cut_off = float('inf')
    if n > 3:
        cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        for edge in range(v+1,n):
            w = random.uniform(0, 1)
            if w < cut_off:
                graph[v].append((edge, w))
                graph[edge].append((v,w))
    return graph, -1

def hypercube_no_w(n):
    graph = [[] for _ in range(n)]
    cut_off = 0.45 + 1/(n**(1/4))
    for i in range(n):
        for j in range(i+1,n):
                if i != j:
            #print(abs(i - j))
                    w = np.random.uniform(0, 1)
                    if w < cut_off:
                        if math.log(abs(i - j), 2).is_integer():
                            graph[i].append((j,w))
                            graph[j].append((i,w))
    return graph, -1

def uniformly_no_w(n):
    graph = [[]for _ in range(n)]
    points = np.zeros((n,2))
    # remove large edges
    cut_off = 3/(n**(1/2))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        points[i] = x,y
    for i in range(n):
        (x1,y1) = points[i]
        for j in range(i+1, n):
            x2,y2 = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
            if dist < cut_off:
                graph[i].append((j,dist))
                graph[j].append((i,dist))
    return graph, -1
                                
def graph_cube3_no_w(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = [[] for _ in range(n)]
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
        for j in range(i+1,n):
            (x2,y2,z2) = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                graph[i].append((j,dist))
                graph[j].append((i, dist))
    return graph, -1

def graph_cube4_no_w(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = [[] for _ in range(n)]
    points = np.zeros((n,4))
    cut_off = 2/(n**(1/4))
    # save points
    for i in range(n):
        w = np.random.uniform(0, 1)
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (w,x,y,z)
    # make graph
    for i in range(n):
        (w1,x1,y1,z1) = points[i]
        for j in range(i+1, n):
            (w2,x2,y2,z2) = points[j]
            dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                graph[i].append((j,dist))
                graph[j].append((i,dist))
    return graph, n

def graph_basic_no_wk(n):
    # input: int n (number of vertices)
    # output: adj. list of graph with some edges cut, 
    #         edges as tuple (target, weight)
    #         weight chosen uniformly at random in [0,1]
    graph = []
    # decide edges to ignore
    cut_off = float('inf')
    if n > 3:
        cut_off = 20*(1/(n-1)-1/((n-1)**2))
    # edge from every v to every w except itself, add random weight
    for v in range(n):
        for edge in range(v+1,n):
            w = random.uniform(0, 1)
            if w < cut_off:
                graph.append(((v,edge), w))
    return graph, n

def hypercube_no_wk(n):
    graph = []
    cut_off = 0.45 + 1/(n**(1/4))
    for i in range(n):
        for j in range(i+1,n):
                if i != j:
            #print(abs(i - j))
                    w = np.random.uniform(0, 1)
                    if w < cut_off:
                        if math.log(abs(i - j), 2).is_integer():
                            graph.append(((i,j),w))
    return graph, n

def uniformly_no_wk(n):
    graph = []
    points = np.zeros((n,2))
    # remove large edges
    cut_off = 3/(n**(1/2))
    for i in range(n):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        points[i] = x,y
    for i in range(n):
        (x1,y1) = points[i]
        for j in range(i+1, n):
            x2,y2 = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
            if dist < cut_off:
                graph.append(((i,j),dist))
    return graph, n
                                
def graph_cube3_no_wk(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = []
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
        for j in range(i+1,n):
            (x2,y2,z2) = points[j]
            dist = np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                graph.append(((i,j),dist))
    return graph, n

def graph_cube4_no_wk(n):
    # input: int n (number of vertices)
    # output: adj. matrix of graph, dict of weights
    graph = []
    points = np.zeros((n,4))
    cut_off = 2/(n**(1/4))
    # save points
    for i in range(n):
        w = np.random.uniform(0, 1)
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        z = np.random.uniform(0, 1)
        points[i] = (w,x,y,z)
    # make graph
    for i in range(n):
        (w1,x1,y1,z1) = points[i]
        for j in range(i+1, n):
            (w2,x2,y2,z2) = points[j]
            dist = np.sqrt((w2-w1)**2+(x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            if dist < cut_off:
                graph.append(((i,j),dist))
    return graph, n
