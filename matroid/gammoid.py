from collections import deque
import copy

class Gammoid:
  def __init__(self, vertices: frozenset, edges: frozenset[tuple], starting_vertices: frozenset, destination_vertices: frozenset):
    dual_vertices, dual_edges, self.dual_starting_vertices, self.dual_destination_vertices = self.derive_dual_representation(vertices, edges, starting_vertices, destination_vertices)
    self.dual_flow_network = FlowNetwork(dual_vertices, dual_edges, self.dual_starting_vertices, self.dual_destination_vertices)
  
  def derive_dual_representation(self, vertices, edges, starting_vertices, destination_vertices):
    flow_network = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)
    base, base_paths = self.base(flow_network, starting_vertices)
    edges, destination_vertices = self.derive_base_representation(base, base_paths, edges)
    vertices, edges = self.derive_duality_respecting_representation(vertices, edges, starting_vertices, destination_vertices)
    edges = self.reverse_edges(edges)
    return vertices, edges, starting_vertices, starting_vertices.difference(destination_vertices)
  
  def base(self, flow_network, starting_vertices):
    base = []
    base_paths = []
    for s in starting_vertices:
      path = flow_network.find_augmenting_path(s)
      if not path: break
      base.append(s)
      base_paths.append(path)
      flow_network.augment_flow(path)
    return (base, base_paths)
    
  def derive_base_representation(self, base, base_paths, edges):
    v = 't'
    for path in base_paths:
      while v != 's':
        u = path[v]
        if u != 's' and v != 't':
          edges = self.swap((u, v), edges)
        v = u
    return edges, base
  
  def swap(self, swap_edge, edges):
    e, f = swap_edge
    new_edges = []
    for edge in edges:
      u, v = edge
      if u != e: new_edges.append((u, v))
      elif u == e and v != f: new_edges.append((f, v))
      elif u == e and v == f: new_edges.append((f, e))
    return frozenset(new_edges)
    
  def derive_duality_respecting_representation(self, vertices, edges, starting_vertices, destination_vertices):
    new_vertices = []
    new_edges = []
    for v in vertices:
      if v in vertices: new_vertices.append(v + '#')
      if v in destination_vertices or v in starting_vertices:new_vertices.append(v)
    for edge in edges:
      u, v = edge
      new_edges.append((u + '#', v + '#'))
    for v in destination_vertices:
      new_edges.append((v + '#', v))
    for v in starting_vertices.difference(destination_vertices):
      new_edges.append((v, v + '#'))
    return (frozenset(new_vertices), frozenset(new_edges))
      
  def reverse_edges(self, edges):
    new_edges = []
    for edge in edges:
      u, v = edge
      new_edges.append((v, u))
    return frozenset(new_edges)
  
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