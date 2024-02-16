from matroid import Matroid

class GraphicalMatroid(Matroid):
  def __init__(self, vertices: frozenset, edges: frozenset):
    self.edges = edges
    self.graph_components = UnionFind(vertices)

  def cocircuit(self, X: frozenset) -> frozenset:
    for x, y in self.edges.difference(X):
      self.graph_components.union(x, y)
    cocircuit = frozenset()
    for e in X:
      x, y = e
      if not self.graph_components.connected(x, y):
        cocircuit = cocircuit.union(frozenset([e]))
    return cocircuit
  
  def contract(self, X: frozenset):
    self.delete(X)
    for x, y in X:
      self.graph_components.union(x, y)

  def delete(self, X: frozenset):
    self.edges = frozenset(edge for edge in self.edges if not edge in X)

class UnionFind:
    def __init__(self, vertices: frozenset):
        self.parent_map = {vertex: None for vertex in vertices}
        
    def find(self, x: str):
        parent = self.parent_map[x]
        if not parent:
            return x
        return self.find(parent)
    
    def union(self, x: str, y: str):
      root_x = self.find(x)
      root_y = self.find(y)
      if root_x != root_y:
        self.parent_map[root_y] = root_x
     
    def connected(self, x: str, y: str):
        return self.find(x) == self.find(y)