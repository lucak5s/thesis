import networkx as nx
import copy

class PlanarMatroid:
  def __init__(self, edges: frozenset):
    networkx_edges = [tuple(e) for e in edges]
    self.graph = nx.MultiGraph(networkx_edges)
    self.dual_graph, self.edges_map = self.derive_dual_representation(self.graph)
    
  def is_empty(self):
    return len(self.dual_graph.edges()) == 0

  def derive_dual_representation(self, graph):
    is_planar, embedding = nx.check_planarity(graph)
    if is_planar:
        return self.build_dual_graph(embedding)
    else:
        print("The graph is not planar and cannot have a dual graph.")
  
  def build_dual_graph(self, embedding):
    dual_graph = nx.MultiGraph()
    edges_map = {}
    visited_edges = set()

    for v in embedding.nodes():
        for w in embedding.neighbors_cw_order(v):         
            if frozenset({v, w}) in visited_edges: continue
            visited_edges.add(frozenset({v, w}))

            right_face = embedding.traverse_face(v, w)
            left_face = embedding.traverse_face(w, v)

            right_face_node = frozenset(right_face)
            left_face_node = frozenset(left_face)

            dual_graph.add_node(right_face_node)
            dual_graph.add_node(left_face_node)

            dual_graph.add_edge(right_face_node, left_face_node, key=frozenset({v, w}))
            edges_map[frozenset({v, w})] = (right_face_node, left_face_node, frozenset({v, w}))
    return (dual_graph, edges_map)

  def cocircuit(self, X: frozenset) -> frozenset:
    edges = [self.edges_map[e] for e in X]
    subgraph = self.dual_graph.edge_subgraph(edges)
    
    # parallel edges or loops
    for u, v in subgraph.edges():
      if subgraph.number_of_edges(u, v) > 1 or u == v: 
        edge_data = subgraph.get_edge_data(u, v)
        circuit = list(edge_data.keys())
        return circuit
        
    # cycle test
    def dfs(current, parent, visited, stack):
        visited.add(current)
        stack.append(current)
        for neighbor in subgraph.neighbors(current):
            if neighbor not in visited:
                parent[neighbor] = current
                cycle = dfs(neighbor, parent, visited, stack)
                if cycle:
                    return cycle
            elif neighbor in visited and neighbor != parent[current]:
                cycle_index = stack.index(neighbor)
                cycle_nodes = stack[cycle_index:] + [neighbor]
                cycle_edges = []
                for i in range(len(cycle_nodes) - 1):
                    u = cycle_nodes[i]
                    v = cycle_nodes[i + 1]
                    key = next(iter(subgraph[u][v])) 
                    cycle_edges.append((u, v, key))
                return cycle_edges
        stack.pop()
        return None

    visited = set()
    parent = {}
    for node in subgraph.nodes():
        if node not in visited:
            cycle = dfs(node, parent, visited, [])
            if cycle:
                return [e[2] for e in cycle]
    return None
    
  def delete(self, element):
    u, v, k = self.edges_map[element]
    if not self.dual_graph.has_edge(u, v, k): return 
    
    self.dual_graph.remove_edge(u, v, k)
    
    neighbors = copy.deepcopy(self.dual_graph.neighbors(v))
    for node in neighbors:
        for key in self.dual_graph[v][node]:
            self.edges_map[key] = (u, node, key)
            self.dual_graph.add_edge(u, node, key=key, **self.dual_graph[v][node][key])
                    
    self.dual_graph.remove_node(v)

  def contract(self, element):
    u, v, k = self.edges_map[element]
    if not self.dual_graph.has_edge(u, v, k): return 

    self.dual_graph.remove_edge(u, v, k)
