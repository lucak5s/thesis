from matroids.matroid import Matroid

groundset = frozenset([1, 2, 3, 4])
independent_sets = frozenset([
  frozenset([1, 2]),
  frozenset([1, 3]),
  frozenset([2, 3]),
  frozenset([1]),
  frozenset([2]),
  frozenset([3]),
  frozenset()
])

matroid = Matroid(groundset, independent_sets)

print(matroid.cocircuit(frozenset([1, 2])))