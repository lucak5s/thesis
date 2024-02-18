from itertools import combinations

def independent_sets_from_bases(bases: frozenset[frozenset]):
  independent_sets = frozenset()
  for base in bases:
    subsets = frozenset(frozenset(subset) for r in range(len(base) + 1) for subset in combinations(base, r))
    independent_sets = independent_sets.union(subsets)
  return independent_sets
