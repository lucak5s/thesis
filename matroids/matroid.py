class Matroid:
  def __init__(self, groundset: frozenset, independent_sets: frozenset[frozenset]):
    self.groundset = groundset
    self.independent_sets = independent_sets
    self.contracted_elements = frozenset()
  
  def independence_oracle(self, X: frozenset) -> bool:
    Y = X.union(self.contracted_elements) 
    return Y in self.independent_sets
  
  def cocircuit(self, X: frozenset) -> frozenset:
    S = frozenset()
    for e in self.groundset.difference(X):
      Y = S.union(frozenset([e]))
      if self.independence_oracle(Y):
        S = Y
    cocircuit = frozenset()
    for e in X:
      Y = S.union(frozenset([e]))
      if self.independence_oracle(Y):
        cocircuit = cocircuit.union(frozenset([e]))
    return cocircuit
  
  def contract(self, X: frozenset) -> frozenset:
    self.contracted_elements = self.contracted_elements.union(X)