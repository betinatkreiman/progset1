import sys
import time
import matplotlib.pyplot as plt
import graphs as gs
import algorithms as algs

# input to command line: python3 progset.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name, flag, numpoints, numtrials, dimension = sys.argv

graph_fxns = {0: gs.graph_basic, 1: gs.hypercube, 2: gs.uniformly, 3: gs.graph_cube3, 4: gs.graph_cube4}

def avg_weight(alg, type_graph, n, trials):
  avg = 0
  for _ in range(trials):
    g, w = type_graph(n)
    alg(g, w)
    # todo: compute average weight
  return (avg / trials)
# avg = avg_weight(algs.prims, graph_fxns[dimension], numpoints, numtrials)
# print(avg, numpoints, numtrials, dimension)

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

def make_weights_plot(name, alg):
  for i in range(1, 20):
    avg = avg_weight(alg, graph_fxns[dimension], i, numtrials)
    plt.scatter(i, avg, c='b')

  plt.xlabel('n vertices')
  plt.ylabel('Avg. MST weight (s)')
  plt.title(name)

  plt.show()