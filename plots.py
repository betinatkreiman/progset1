import matplotlib.pyplot as plt
import time
'''


def make_time_plot(name, ts, ns):

  plt.plot()

  plt.plot(ns, ts)

  plt.xlabel('n vertices')
  plt.ylabel('Avg. run-time (s)')
  plt.title(name)

  plt.show()

def max_edge_p(name):
  for i in range(1, 40):
    # change to do by powers of 2
    # this plots the max edge weight in the mst
    max = max_weight_p(graph_fxns[dimension], i, numtrials)
    plt.scatter(i, max, c='b')

  plt.xlabel('2^x vertices')
  plt.ylabel('Av.g max MST weight')
  plt.title(name)

  plt.show()

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
'''