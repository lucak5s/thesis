from typing import List, Tuple

class PartitionMatroid:
  def __init__(self, groundset: frozenset, partitions: List[Tuple[frozenset, int]]):
    self.groundset = groundset
    self.partitions = partitions
    
  def is_empty(self):
    return len(self.groundset) == 0

  def cocircuit(self, X: frozenset) -> frozenset:
    cocircuit = None
    for partition in self.partitions:
      S = partition[0].intersection(X)
      if len(S) == len(partition[0]) - partition[1] + 1:
        return S
    return frozenset()
  
  def delete(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    for i in range(len(self.partitions)):
      partition = self.partitions[i]
      if item in partition[0]:
        new_partition = frozenset(element for element in partition[0] if element != item)
        self.partitions[i] = (new_partition, partition[1])

  def contract(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    for i in range(len(self.partitions)):
      partition = self.partitions[i]
      if item in partition[0]:
        new_partition = frozenset(element for element in partition[0] if element != item)
        new_k = partition[1] - 1
        self.partitions[i] = (new_partition, new_k)

