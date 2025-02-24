import sys
import time
import matplotlib.pyplot as plt
import graphs as gs
import algorithms as algs

# input to command line: python3 progset.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name_s, flag_s, numpoints_s, numtrials_s, dimension_s = sys.argv
numpoints = int(numpoints_s)
numtrials = int(numtrials_s)
dimension = int(dimension_s)

graph_fxns = {0: gs.graph_basic, 1: gs.hypercube, 2: gs.uniformly, 3: gs.graph_cube3, 4: gs.graph_cube4}

# compute the average weight of type_graph on n vertices over trials
# using kruskal's alg
def avg_weight_k(type_graph, n, trials):
  avg = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, mstweight, _ = algs.kruskals(g, w)
    avg += mstweight
  return (avg / trials)
#avg = avg_weight_k(graph_fxns[dimension], numpoints, numtrials)
#print(avg, numpoints, numtrials, dimension)

def max_weight_k(type_graph, n, trials):
  max = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, max_edge = algs.kruskals(g, w)
    max += max_edge
  return (max / trials)

def run(alg, type_graph, ns, numb_times):
  times = []

  for n in ns:
    current_time = 0
    for _ in range(numb_times):

      g, w = type_graph(n)

      start = time.time()
      alg(g, w, 0)
      end = time.time()

      current_time += end - start

    current_time /= numb_times
    times.append(current_time)

  return times

def make_time_plot(name, ts, ns):

  plt.plot()

  plt.plot(ns, ts)

  plt.xlabel('n vertices')
  plt.ylabel('Avg. run-time (s)')
  plt.title(name)

  plt.show()

def make_weights_plot(name):
  for i in range(10, 50):
    # change to do by powers of 2
    max = max_weight_k(graph_fxns[dimension], i, numtrials)
    plt.scatter(i, max, c='b')

  plt.xlabel('n vertices')
  plt.ylabel('Avg. MST weight (s)')
  plt.title(name)

  plt.show()
make_weights_plot("max!")