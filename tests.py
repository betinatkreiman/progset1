import algorithms as algs
import datastructures as ds
import numpy as np
import plots as ps

def union_find_test():
    dus10a = ds.DisjointUnionSets(5)
    for i in range(5):
        assert dus10a.parent[i] == i, "initialized parents failed"
    dus10a.union(0,2)
    assert (np.array_equal(dus10a.parent, np.array([2,1,2,3,4]))), "basic union failed"
    dus10a.union(2,3)
    assert (np.array_equal(dus10a.parent, np.array([2,1,2,2,4]))), "second union failed"
    dus10a.union(1,4)
    dus10a.union(2,4)
    assert (np.array_equal(dus10a.parent, np.array([2,4,4,2,4]))), "union trees failed"
    print("union tests passed")


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
    
def kruskal_spanning_test(gfn):
    # takes in a graph function
    # insures the output of kruskals is a spanning tree

    # run 10 times on random graph of j vertices
    for i in range(10):
        for j in range(10, 50):
            # V = set of vertices included in X
            V = set()
            g, w = gfn(j)
            _, X, _, _ = algs.kruskals(g, w, 0)
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

def kruskal_mst_weight(gfn):
    # test if the weight of the mst is <= total weight of graph
    for _ in range(10): 
        for j in range(2, 50):
            g,w = gfn(j)
            _, _, mstweight, _ = algs.kruskals(g,w, 0)
            total_w = sum(w.values())
            if total_w < mstweight:
                raise ValueError("mst is too big kruskal")
    print("kruskal mst weight passed")

# run tests
union_find_test()
for key in ps.graph_fxns:
    graph = ps.graph_fxns[key]
    # graph_test(graph)
    # prim_spanning_test(graph)
    kruskal_spanning_test(graph)
    kruskal_mst_weight(graph)