class UniformMatroid:
  def __init__(self, groundset: frozenset, k: int):
    self.groundset = groundset
    self.k = k
    
  def is_empty(self):
    return len(self.groundset) == 0

  def cocircuit(self, X: frozenset) -> frozenset:
    if len(X) != len(self.groundset) - self.k + 1: return frozenset()
    return X

  def delete(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
  
  def contract(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    self.k -= 1

