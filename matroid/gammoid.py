from collections import deque
import copy

class Gammoid:
  def __init__(self, vertices: frozenset, edges: frozenset[tuple], starting_vertices: frozenset, destination_vertices: frozenset):
    self.starting_vertices = starting_vertices
    self.destination_vertices = destination_vertices
    self.flow_network = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)

    base = self.random_base()
    self.full_rank = len(base)

    dual_vertices, dual_edges, dual_starting_vertices, dual_destination_vertices = self.derive_dual_matroid()
    self.dual_starting_vertices = dual_starting_vertices
    self.dual_destination_vertices = dual_destination_vertices
    self.dual_flow_network = FlowNetwork(dual_vertices, dual_edges, dual_starting_vertices, dual_destination_vertices)
 
  def random_base(self):
    pass

  def derive_dual_matroid(self):
    pass

  def cocircuit(self, X: frozenset) -> frozenset:
    pass
  
  def delete(self, element):
    pass

  def contract(self, element):
    pass


class FlowNetwork():
  def __init__(self, vertices, edges, sources, sinks):
    self.graph = {}
    for v in vertices:
      self.add_edge(v + '_in', v + '_out', 1)
    for u, v in edges:
      self.add_edge(u + '_out', v + '_in', 1)
    for v in sources:
      self.add_edge('source', v + '_in', 1)
    for v in sinks:
      self.add_edge(v + '_out', 'sink', 1)

  def add_edge(self, u, v, weight):
    if u not in self.graph:
      self.graph[u] = {}
    if v not in self.graph:
      self.graph[v] = {} 
    self.graph[u][v] = weight 
    self.graph[v][u] = 0 

  def set_sink_weight(self, v, weight):
    self.graph[v + '_out']['sink'] = weight

  def find_augmenting_path(self, element=None):
    parent = {}
    visited = set({'source'})
    queue = deque(['source'])
    while queue:
      u = queue.popleft()
      for v, capacity in self.graph[u].items():
        if v not in visited and capacity > 0:
          visited.add(v)
          parent[v] = u
          if v == 'sink':
            if element and element + '_out' != u: continue
            return parent
          queue.append(v)
    return None
      
  def augment_flow(self, path):
    v = 'sink'
    while v != 'source':
      u = path[v]
      self.graph[u][v] = 0
      self.graph[v][u] = 1
      v = path[v]