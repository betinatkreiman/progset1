class DisjointUnionSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, i):
        root = self.parent[i]
        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]
        return root

    def unionSets(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return 
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

def betina_heap(diction):
  min_val = list(diction.values())[0]
  min_index = 0
  for i in range(len(diction)):
    if list(diction.values())[i] < min_val:
      min_val = list(diction.values())[i]
      min_index = i
  return list(diction.keys())[min_index], min_index