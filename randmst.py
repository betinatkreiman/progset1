import sys
import time

# input to command line: progset.py 0 numpoints numtrials dimension
# output: average numpoints numtrials dimension
program_name, flag, numpoints, numtrials, dimension = sys.argv

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

import matplotlib.pyplot as plt

def make_plot(name, ts, ns):

  plt.plot()

  plt.plot(ns, ts)

  plt.xlabel('n vertices')
  plt.ylabel('Avg. run-time (s)')
  plt.title(name)

  plt.show()