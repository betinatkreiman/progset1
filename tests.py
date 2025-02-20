import graphs as g

def graph_test(fn):
    # takes in a graph function and ensures the output is 
    # an undirected, complete graph
    for i in range(5, 20):
        graph, weight = fn(i)
        for v in range(i):
            for w in range(i):
                if (graph[v][w] != 1) and (v != w):
                    raise ValueError("Not a complete graph")
                if weight[(v,w)] != weight[(w,v)]:
                    raise ValueError("Graph is not undirected")
    print("graph_test passsed")
    return

# run tests
graph_test(g.graph_basic)