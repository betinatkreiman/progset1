import sys
import graphs as gs
import algorithms as algs
import plots as ps
import time

# input to command line: python3 randmst.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name_s, alg_flag_s, numpoints_s, numtrials_s, dimension_s = sys.argv
alg_flag = int(alg_flag_s)
numpoints = int(numpoints_s)
numtrials = int(numtrials_s)
dimension = int(dimension_s)

def avg_weight(dim, n, trials):
  # algorithm = ps.alg_choice_no[alg_flag]
  type_graph = ps.graph_fxns_no_g[dim]
  avg = 0
  for _ in range(trials):
    g,w = type_graph(n)
    _, _, mstweight, _ = algs.kruskals_no_g(g,w,0)
    # if mstweight == float('inf'):
    #  continue
    avg += mstweight
  return (avg / trials)

# ps.compare_graphs()
# ps.max_edge_plot(alg_flag, dimension, numtrials)
avg = avg_weight(dimension, numpoints, numtrials)
# avg2 = avg_weight(alg_flag, 5, numpoints, numtrials)
print(avg, numpoints, numtrials, dimension)
# print(avg2, numpoints, numtrials, dimension)

'''
kruskals: (generally faster than prims, but only once edges are cut from complete graphs)
  basic: all!
  hyper: 4096 (sometimes)
  2d: 4096
  3d: 4096
  4d: 4096

prims:
  basic: all!
  hyper: 4096 
  2d: 4096
  3d: 4096
  4d: 4096
'''