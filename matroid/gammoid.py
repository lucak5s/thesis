from collections import deque
import copy

class Gammoid:
  def __init__(self, vertices: frozenset, edges: frozenset[tuple], starting_vertices: frozenset, destination_vertices: frozenset):
    self.starting_vertices = starting_vertices
    self.destination_vertices = destination_vertices
    self.flow_network = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)

    base = self.base()

    dual_vertices, dual_edges, dual_starting_vertices, dual_destination_vertices = self.derive_dual_representation()
    self.dual_starting_vertices = dual_starting_vertices
    self.dual_destination_vertices = dual_destination_vertices
    self.dual_flow_network = FlowNetwork(dual_vertices, dual_edges, dual_starting_vertices, dual_destination_vertices)
 
  def base(self):
    pass

  def derive_base_representation(self):
    pass

  def derive_dual_representation(self):
    pass

  def cocircuit(self, X: frozenset) -> frozenset:
    pass
  
  def delete(self, element):
    pass

  def contract(self, element):
    pass


class FlowNetwork():
  def __init__(self, vertices, edges, starting_vertices, destination_vertices):
    self.graph = {}
    for v in vertices:
      self.add_edge(v + '_in', v + '_out', 1)
    for u, v in edges:
      self.add_edge(u + '_out', v + '_in', 1)
    for v in starting_vertices:
      self.add_edge('s', v + '_in', 1)
    for v in destination_vertices:
      self.add_edge(v + '_out', 't', 1)

  def add_edge(self, u, v, weight):
    if u not in self.graph:
      self.graph[u] = {}
    if v not in self.graph:
      self.graph[v] = {} 
    self.graph[u][v] = weight 
    self.graph[v][u] = 0 

  def find_augmenting_path(self, element=None):
    parent = {}
    visited = set({'s'})

    if element:
      visited.add(element + '_in')
      parent[element + '_in'] = 's'
      queue = deque([element + '_in'])
    else:
      queue = deque(['s'])

    while queue:
      u = queue.popleft()
      for v, capacity in self.graph[u].items():
        if v not in visited and capacity > 0:
          visited.add(v)
          parent[v] = u
          if v == 't': return parent
          queue.append(v)
    return None
      
  def augment_flow(self, path):
    v = 't'
    while v != 's':
      u = path[v]
      self.graph[u][v] = 0
      self.graph[v][u] = 1
      v = path[v]