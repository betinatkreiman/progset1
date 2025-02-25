import numpy as np

class DisjointUnionSets:
   def __init__ (self, n):
      self.rank = np.zeros(n)
      self.parent = np.arange(0,n)
   
   def find(self, x):
      p = self.parent[x]
      if p == x:
         return x
      else:
         return self.find(p)
   
   def link(self, x, y):
      rank_x = self.rank[x]
      rank_y = self.rank[y]
      if rank_x > rank_y:
         x, y = y, x
      if rank_x == rank_y:
         self.rank[y] += 1
      self.parent[x] = y
   
   def union(self, x, y):
      self.link(self.find(x), self.find(y))


class Heap:
  def init(self, n):
    # creates an empty heap
    self.heap = []
    self.size = 0

  #def create(H):
    # creates an empty heap

  def minheapify(self, n):
    left = 2* n
    right = 2* n + 1

    if left < self.size and self.heap[left][1] < self.heap[n][1]:
      min_index = left
    else:
      min_index = n
      #print("else", min_index, n)

    if right < self.size and self.heap[right][1] < self.heap[min_index][1]:
      min_index = right
      #print("if", min_index, n)


    #print("left", left)
    #print("right", right)
    #print(min_index, n)
    #print("values", self.heap[min_index], self.heap[n])

    if min_index != n:
      temp = self.heap[min_index]
      self.heap[min_index] = self.heap[n]
      self.heap[n] = temp

      #print("NEW HEAP", self.heap)
      #return None
      self.minheapify(min_index)


    return

  def insert(self, p, w):
    # inserts a new object x with value y pair in the structure H
    # self.heap[x] = y
    # self.size += 1

    self.size += 1
    self.heap.append([p, w])
    n = self.size - 1

    #print(self.heap)
    #print(self.heap[n][1])

    while n != 0 and self.heap[n][1] < self.heap[math.floor(n/2)][1]:
      temp = self.heap[n]
      self.heap[n] = self.heap[math.floor(n/2)]
      self.heap[math.floor(n/2)] = temp
      n = math.floor(n/2)

    # while n != 0 and self.heap[p] < self.heap[list(self.heap.keys())[math.floor(n/2)]]:
    #   temp = self.heap[p]
    #   self.heap[p] = self.heap[list(self.heap.keys())[math.floor(n/2)]]
    #   self.heap[list(self.heap.keys())[math.floor(n/2)]] = temp
    #   n = math.floor(n/2)



  def buildheap(self):
    # self is dictionary
    # for i in range(math.floor(len(self.heap)/2), 1):
    #   self.minheapify(self, pair, weight)

    for i in range(math.floor(self.size/2), 1, -1):
      self.minheapify(i)

  def extractmin(self):
    # if self.size > 0:
    #   min_weight = list(self.heap.values())[0]
    #   min_pair = list(self.heap.keys())[0]

    #   self.heap[min_pair] = list(self.heap.keys())[self.size - 1]

    #   self.size -= 1

    #   self.minheapify(self, min_pair, min_weight)

    #   return min_pair, min_weight
    # else:
    #   return None

    if self.size > 0:
      min = self.heap[0]
      self.heap[0] = self.heap[self.size-1]
      self.size -= 1

      self.heap.pop()
      self.minheapify(0)
      return min
    else:
      return None

  #def change(H, x, y):
    # if y is smaller than the current value of x in H then change the value of x in H to y

  #def deletemin(self):
    # return the object with smallest value in H

