import copy

class GraphicMatroid:
  def __init__(self, vertices: frozenset, edges: frozenset):
    self.vertices = vertices
    self.edges = edges
    self.graph_components = UnionFind(vertices)

  def unique_cocircuit(self, X: frozenset) -> frozenset:
    graph_components = copy.deepcopy(self.graph_components)
    for x, y in self.edges.difference(X):
      graph_components.union(x, y)
    cocircuit = frozenset()
    for e in X:
      x, y = e
      if not graph_components.connected(x, y):
        cocircuit = cocircuit.union(frozenset([e]))
    return cocircuit
  
  def contract(self, element):
    self.delete(element)
    x, y = element
    self.graph_components.union(x, y)

  def delete(self, element):
    self.edges = frozenset(edge for edge in self.edges if edge != element)

class UnionFind:
  def __init__(self, vertices: frozenset):
    self.parent_map = {vertex: vertex for vertex in vertices}
    self.rank = {vertex: 0 for vertex in vertices}
  
  def find(self, x):
    if self.parent_map[x] != x:
      self.parent_map[x] = self.find(self.parent_map[x])
    return self.parent_map[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      if self.rank[root_x] < self.rank[root_y]:
        self.parent_map[root_x] = root_y
      elif self.rank[root_x] > self.rank[root_y]:
        self.parent_map[root_y] = root_x
      else:
        self.parent_map[root_y] = root_x
        self.rank[root_x] += 1

  def connected(self, x, y) -> bool:
    return self.find(x) == self.find(y)
  
  def count_components(self) -> int:
    unique_roots = {self.find(vertex) for vertex in self.parent_map}
    return len(unique_roots)