import graphs as gs
import algorithms as alg
import random

def graph_test(gfn):
    # takes in a graph function and ensures the output is 
    # an undirected, complete graph
    for i in range(10, 50):
        graph, weight = gfn(i)
        for v in range(i):
            for w in range(i):
                if v != w:
                    if (graph[v][w] != 1):
                        raise ValueError("Not a complete graph")
                    if weight[(v,w)] != weight[(w,v)]:
                        raise ValueError("Graph is not undirected")
    print("graph_test passsed")
    return

def prim_spanning_test(gfn):
    # takes in a graph function
    # insures the output of prim is a spanning tree

    # run 10 times on random graph of j vertices
    for i in range(10):
        for j in range(10, 50):
            graph, weight = gfn(i)
            source = random.randint(0, j-1)
            d, prev = alg.prims(graph, weight, 0)
    return -1

def kruskal_spanning_test(gfn):
    # takes in a graph function
    # insures the output of kruskals is a spanning tree

    # run 10 times on random graph of j vertices
    for i in range(10):
        for j in range(10, 50):
            # V = set of vertices included in X
            V = set()
            graph, weight = gfn(j)
            X = alg.kruskals(graph, weight)
            for (u,v) in X:
                V.add(u)
                V.add(v)
            # ensure V includes all vertices of graph
            All = set(range(j))
            if V != All:
                missing = All.difference(V)
                raise ValueError("Tree does not contain: ", missing)
    print("kruskal spanning test passed")
    return

# run tests
kruskal_spanning_test(gs.graph_cube4)