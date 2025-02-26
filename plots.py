import matplotlib.pyplot as plt
import time
import numpy as np
import graphs as gs
import algorithms as algs
import math

graph_fxns = {0: gs.graph_basic_faster, 1: gs.hypercube_faster, 2: gs.uniformly_faster, 3: gs.graph_cube3_faster, 4: gs.graph_cube4_faster}
alg_choice = {0: algs.prims_adj_list, 1: algs.kruskals}

def max_edge_weight(alg_flag, dimension, n, trials):
    type_graph = graph_fxns[dimension]
    algorihtm = alg_choice[alg_flag]
    max = 0
    for _ in range(trials):
        g, w = type_graph(n)
        _, _, _, max_edge = algorihtm(g, w, 0)
        if max_edge > max:
            max = max_edge
    return max

def max_edge_plot(alg_flag, dimension, trials):
    for a in range(1, 13):
        n = 2**a
        # change to do by powers of 2
        # this plots the max edge weight in the mst
        max = max_edge_weight(alg_flag, dimension, n, trials)
        plt.scatter(n, max, c='b')
        # edit this one:
        plt.scatter(n,20*(1/(n-1)-1/((n-1)**2)), c='r')
        print(n, max, 20*(1/(n-1)-1/((n-1)**2)))
    if alg_flag == 0:
       algorithm = "Prims"
    else:
       algorithm = "Kruskals"
    plt.xlabel('number of vertices')
    plt.ylabel('Max MST edge weight across trials')
    plt.title(f"{algorithm} Max Edge Weight for Dimension {dimension}")
    plt.show()
# python3 randmst.py 1 3 20 0
    
def run(alg, type_graph, ns, numb_times):
    times = []

    for n in range(4, ns):
        current_time = 0
        for _ in range(numb_times):
            g, w = type_graph(n)

            start = time.time()
            alg(g, w, 0)
            end = time.time()

            current_time += end - start

        current_time /= numb_times
        times.append([n, current_time])

    return times

def compare_graphs(alg_choice):
    n = 100
    t = 20
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
