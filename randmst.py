import sys
import graphs as gs
import algorithms as algs

# input to command line: python3 progset.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name_s, flag_s, numpoints_s, numtrials_s, dimension_s = sys.argv
numpoints = int(numpoints_s)
numtrials = int(numtrials_s)
dimension = int(dimension_s)

graph_fxns = {0: gs.graph_basic, 1: gs.hypercube, 2: gs.uniformly, 3: gs.graph_cube3, 4: gs.graph_cube4}

def avg_weight_p(type_graph, n, trials):
  avg = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, mstweight, _ = algs.prims(g,w,0)
    avg += mstweight
  return (avg / trials)

def max_weight_p(type_graph, n, trials):
  max = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, _, max_edge = algs.prims(g, w, 0)
    max += max_edge
  return (max / trials)

# compute the average weight of type_graph on n vertices over trials
# using kruskal's alg
def avg_weight_k(type_graph, n, trials):
  avg = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, mstweight, _ = algs.kruskals(g, w)
    avg += mstweight
  return (avg / trials)

avg = avg_weight_k(graph_fxns[dimension], numpoints, numtrials)
print(avg, numpoints, numtrials, dimension)