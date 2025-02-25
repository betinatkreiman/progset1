import matplotlib.pyplot as plt
import time
import numpy as np
import graphs as gs
import algorithms as algs

graph_fxns = {0: gs.graph_basic_faster, 1: gs.hypercube, 2: gs.uniformly, 3: gs.graph_cube3, 4: gs.graph_cube4}
alg_choice = {0: algs.prims_adj_list, 1: algs.kruskals}

def max_edge_weight(alg_flag, dimension, n, trials):
  max = 0
  for _ in range(trials):
    g, w = graph_fxns[dimension](n)
    _, _, _, max_edge = alg_choice[alg_flag](g, w, 0)
    max += max_edge
  return (max / trials)

def max_edge_plot(alg_flag, dimension, trials):
    for i in range(3, 100):
        # change to do by powers of 2
        # this plots the max edge weight in the mst
        max = max_edge_weight(alg_flag, dimension, i, trials)
        plt.scatter(i, max, c='b')
        j = i
        if i > 10:
           j = i - 10
        # edit this one:
        plt.scatter(i, 1/np.sqrt(j), c='r')
    if alg_flag == 0:
       algorithm = "Prims"
    else:
       algorithm = "Kruskals"
    plt.xlabel('number of vertices')
    plt.ylabel('Avg max MST edge weight')
    plt.title(f"{algorithm} Max Edge Weight for Dimension {dimension}")
    plt.show()
# python3 randmst.py 1 3 20 0
def run(alg, type_graph, ns, numb_times):
    times = []

    for n in range(4, ns):
        current_time = 0
        for _ in range(numb_times):
            g, w = type_graph(2**n)

            start = time.time()
            alg(g, w, 0)
            end = time.time()

            current_time += end - start

        current_time /= numb_times
        times.append([n, current_time])

    return times

def compare_graphs(alg_choice):
    n = 10
    t = 10
    slow = run(alg_choice, gs.graph_basic, n, t)
    fast = run(alg_choice, gs.graph_basic_faster, n, t)
    plt.scatter(*zip(*slow), c='b') 
    plt.scatter(*zip(*fast), c='r') 
    plt.xlabel('number of vertices')
    plt.ylabel('Speed of Alg')
    plt.title(f"Kruskals speed for dimension 0")
    plt.show()

def make_time_plot(name, ts, ns):

  plt.plot()

  plt.plot(ns, ts)

  plt.xlabel('n vertices')
  plt.ylabel('Avg. run-time (s)')
  plt.title(name)

  plt.show()
