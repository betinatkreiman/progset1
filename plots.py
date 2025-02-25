import matplotlib.pyplot as plt
import time
import algorithms as algs
import graphs as gs
import numpy as np

def max_weight_p(type_graph, n, trials):
  max = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, _, max_edge = algs.prims(g, w, 0)
    max += max_edge
  return (max / trials)

def max_weight_k(type_graph, n, trials):
  max = 0
  for _ in range(trials):
    g, w = type_graph(n)
    _, _, max_edge = algs.kruskals(g, w)
    max += max_edge
  return (max / trials)

def max_edge_p(graph_type):
  for i in range(2, 40):
    # change to do by powers of 2
    # this plots the max edge weight in the mst
    max = max_weight_p(graph_type, i, 30)
    plt.scatter(i, max, c='b')

  plt.xlabel('x vertices')
  plt.ylabel('Av.g max MST edge weight')
  plt.title("Prim max edge weight")

  plt.show()

def max_edge_k(graph_type):
    for i in range(2, 80):
        # change to do by powers of 2
        # this plots the max edge weight in the mst
        max = max_weight_k(graph_type, i, 50)
        plt.scatter(i, max, c='b')
        plt.scatter(i, 2/np.sqrt(i), c='r')
    plt.xlabel('x vertices')
    plt.ylabel('Av.g max MST edge weight')
    plt.title("Kruskal max edge weight")
    plt.show()

max_edge_k(gs.graph_basic)

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
