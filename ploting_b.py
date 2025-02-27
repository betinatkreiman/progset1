

def plot_values(alg, type_graph, ns, numb_times):
  avgs = []

  for n in ns:
    new_avg = 0
    for _ in range(numb_times):
      g, w = type_graph(n)
      d, prev, mst_weight, max = alg(g, w, 0) # for prims
      # X, mst_weight, sort_w = alg(g, w) # for kruskals

      new_avg += mst_weight

    new_avg = new_avg / numb_times
    avgs.append(new_avg)
  
  print(avgs)

  # plt.plot()
  # plt.plot(ns, avgs)
  # plt.xlabel('n vertices')
  # plt.ylabel('Avg. Value')
  # plt.title("Prims Algorithm (Uniform)")
  # plt.title("Prims Algorithm (Hypercube)")
  # plt.title("Prims Algorithm (2D)")
  # plt.title("Prims Algorithm (3D)")
  # plt.title("Prims Algorithm (4D)")
  # plt.title("Kruskals Algorithm (Uniform)")
  # plt.title("Kruskals Algorithm (Hypercube)")
  # plt.title("Kruskals Algorithm (2D)")
  #plt.title("Kruskals Algorithm (3D)")
  # plt.title("Kruskals Algorithm (4D)")
  # plt.show()

  return

  
#n_uniform = [64, 128, 256, 512, 1024]

#plot_values(algs.prims, gs.graph_cube4, n_uniform, 30)
#plot_values(algs.kruskals, gs.graph_cube4, n_uniform, 30)
#plot_values(algs.prims, gs.graph_basic, [1, 2, 8, 16, 64, 128, 256, 512], 20)

#complete_ns = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
complete_ns = [128, 256, 512, 1024, 2048, 4096]
# final_3 = [8192, 16384, 32768]
final_3 = [8192, 16384]
#hypercube_ns = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]
#hypercube_ns = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

# print("3d")
# plot_values(algs.kruskals, gs.graph_cube3, complete_ns, 5)

# print()
# print("4d")
# plot_values(algs.kruskals, gs.graph_cube4, complete_ns, 5)

print()
print("basic")
plot_values(algs.prims, gs.graph_basic, final_3, 5)

print()
print("unifromly / 2D")
plot_values(algs.prims, gs.uniformly, final_3, 5)

print()
print("3D")
plot_values(algs.prims, gs.graph_cube3, final_3, 5)

print()
print("4D")
plot_values(algs.prims, gs.graph_cube4, final_3, 5)