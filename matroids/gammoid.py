from matroids.matroid import Matroid
from collections import deque
import copy

class Gammoid(Matroid):
  def __init__(self, vertices, edges: frozenset[tuple], sources: frozenset, sinks: frozenset):
    self.flow_network = GammoidFlowNetwork(vertices, edges, sources, sinks)
    self.sinks = sinks

  def full_rank(self) -> int:
    flow_network = copy.deepcopy(self.flow_network)
    rank = 0
    while True:
      path = flow_network.find_augmenting_path()
      if not path: break
      rank += 1
      flow_network.augment_flow(path)
    return rank 

  def unique_cocircuit(self, X: frozenset) -> frozenset:
    flow_network = copy.deepcopy(self.flow_network)

    for e in X:
      flow_network.set_sink_weight(e, 0)

    while True:
      path = flow_network.find_augmenting_path()
      if not path: break
      flow_network.augment_flow(path)
    
    cocircuit = frozenset()
    for e in X:
      flow_network.set_sink_weight(e, 1)
      path = flow_network.find_augmenting_path()
      if path:
        cocircuit = cocircuit.union(frozenset([e]))
      flow_network.set_sink_weight(e, 0)

    return cocircuit
  
  def contract(self, element):
    path = self.flow_network.find_augmenting_path(element)
    self.flow_network.augment_flow(path)

  def delete(self, element):
    self.flow_network.set_sink_weight(element, 0)


class GammoidFlowNetwork():
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