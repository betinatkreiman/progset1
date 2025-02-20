class DisjointUnionSets:
    #todo

def betina_heap(diction):
  min_val = list(diction.values())[0]
  min_index = 0
  for i in range(len(diction)):
    if list(diction.values())[i] < min_val:
      min_val = list(diction.values())[i]
      min_index = i
  return list(diction.keys())[min_index], min_index