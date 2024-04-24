from collections import deque
import copy

class Gammoid:
  def __init__(self, vertices: frozenset, edges: frozenset[tuple], starting_vertices: frozenset, destination_vertices: frozenset):
    dual_vertices, dual_edges, self.dual_starting_vertices, self.dual_destination_vertices = self.derive_dual_representation(vertices, edges, starting_vertices, destination_vertices)
    self.dual_flow_network = FlowNetwork(dual_vertices, dual_edges, self.dual_starting_vertices, self.dual_destination_vertices)
    
  def derive_dual_representation(self, vertices, edges, starting_vertices, destination_vertices):
    flow_network = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)
    base_paths = self.base_paths(flow_network)
    edges, destination_vertices = self.derive_base_representation(base_paths, edges)
    vertices, edges = self.derive_duality_respecting_representation(vertices, edges, starting_vertices, destination_vertices)
    edges = self.reverse_edges(edges)
    return vertices, edges, starting_vertices, starting_vertices.difference(destination_vertices)
  
  def base_paths(self, flow_network):
    base_paths = []
    path = flow_network.find_augmenting_path()
    while path:
      base_paths.append(path)
      flow_network.augment_flow(path)
      path = flow_network.find_augmenting_path()
      
    return base_paths
    
  def derive_base_representation(self, base_paths, edges):
    base = []
    for path in base_paths:
      v = 't'
      while v != 's':
        u = path[v]
        if u.endswith('out') and v.endswith('in'):
          edges = self.swap((u[:-4], v[:-3]), edges)
        if u == 's': base.append(v[:-3])
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
    flow_network = copy.deepcopy(self.dual_flow_network)
    print(flow_network.graph)
    element_path_map = {}
    cocircuit = set()
    
    for e in X:
      path = flow_network.find_augmenting_path(e)
      if path:
        cocircuit.add(e)
        element_path_map[e] = path
        flow_network.augment_flow(path)
      else:
        for f in list(cocircuit):
          f_path = element_path_map[f]
          flow_network.reverse_augment_flow(f_path)
    
          e_path = flow_network.find_augmenting_path(e)
          if not e_path: 
            cocircuit.remove(f)
          else: flow_network.augment_flow(f_path)
      
        cocircuit.add(e)
        return frozenset(cocircuit)
    
    return frozenset()
  
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
      v = u
      
  def reverse_augment_flow(self, path):
    v = 't'
    while v != 's':
      u = path[v]
      self.graph[u][v] = 1
      self.graph[v][u] = 0
      v = u