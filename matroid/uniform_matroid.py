class UniformMatroid:
  def __init__(self, groundset: frozenset, k: int):
    self.groundset = groundset
    self.k = k

  def full_rank(self) -> int:
    return self.k

  def unique_cocircuit(self, X: frozenset) -> frozenset:
    if len(X) != len(self.groundset) - self.k + 1: return frozenset()
    return X
  
  def contract(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    self.k -= 1

  def delete(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    print(self.groundset)

