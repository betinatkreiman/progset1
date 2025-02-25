import sys
import graphs as gs
import algorithms as algs
import plots as ps

# input to command line: python3 randmst.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name_s, alg_flag_s, numpoints_s, numtrials_s, dimension_s = sys.argv
alg_flag = int(alg_flag_s)
numpoints = int(numpoints_s)
numtrials = int(numtrials_s)
dimension = int(dimension_s)

alg_choice = {1: algs.prims, 0: algs.kruskals}
graph_fxns = {0: gs.graph_basic_faster, 1: gs.hypercube, 2: gs.uniformly, 3: gs.graph_cube3_faster, 4: gs.graph_cube4}

def avg_weight(alg_flag, dim, n, trials):
  algorithm = alg_choice[alg_flag]
  type_graph = graph_fxns[dim]
  if alg_flag == 0 and dim == 0:
    algorithm = algs.prims_adj_list
    type_graph = gs.graph_basic_adj_list
  avg = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, mstweight, _ = algorithm(g,w,0)
    avg += mstweight
  return (avg / trials)
# ps.compare_graphs(alg_choice[alg_flag])
# ps.max_edge_plot(alg_flag, dimension, numtrials)
avg = avg_weight(alg_flag, dimension, numpoints, numtrials)
# avg2 = avg_weight(alg_flag, 5, numpoints, numtrials)
print(avg, numpoints, numtrials, dimension)
# print(avg2, numpoints, numtrials, dimension)

'''
kruskals:
  basic: 2048, 4096
  hyper: 4096
  2d: 1024, 2048, 4096
  3d: 1024, 2048, 4096
  4d: 1024, 2048, 4096

prims:
  basic: 4096
  hyper: 4096
  2d: 1024, 2048, 4096
  3d: 1024, 2048, 4096
  4d: 1024, 2048, 4096
'''