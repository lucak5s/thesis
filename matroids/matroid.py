from itertools import combinations

class Matroid:
  def __init__(self, groundset: frozenset, independent_sets: frozenset[frozenset]):
    self.groundset = groundset
    self.independent_sets = independent_sets
    self.contracted_elements = frozenset()
  
  def independence_oracle(self, X: frozenset) -> bool:
    Y = X.union(self.contracted_elements) 
    return Y in self.independent_sets
  
  def rank(self, X: frozenset) -> int:
    S = frozenset()
    for e in X:
      Y = S.union(frozenset([e]))
      if self.independence_oracle(Y):
        S = Y
    return len(S)

  def unique_cocircuit(self, X: frozenset) -> frozenset:
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
  
  def contract(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    self.contracted_elements = self.contracted_elements.union(frozenset([item]))

  def delete(self, item):
    self.groundset = frozenset(element for element in self.groundset if element != item)
    self.independent_sets = frozenset(set for set in self.independent_sets if not item in set)


class BasesMatroid(Matroid):
  def __init__(self, groundset: frozenset, bases: frozenset[frozenset]):
    independent_sets = self.independent_sets_from_bases(bases)
    super().__init__(groundset, independent_sets)

  def independent_sets_from_bases(self, bases: frozenset[frozenset]):
    independent_sets = frozenset()
    for base in bases:
      subsets = frozenset(frozenset(subset) for r in range(len(base) + 1) for subset in combinations(base, r))
      independent_sets = independent_sets.union(subsets)
    return independent_sets
