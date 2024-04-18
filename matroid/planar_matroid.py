import networkx as nx

class PlanarMatroid:
  def __init__(self, edges: frozenset):
    self.graph = nx.Graph(edges)
    self.dual_graph = self.derive_dual_representation(self.graph)

  def derive_dual_representation(self, graph):
    is_planar, embedding = nx.check_planarity(graph)
    if is_planar:
        return self.build_dual_graph(embedding)
    else:
        print("The graph is not planar and cannot have a dual graph.")
  
  def build_dual_graph(self, embedding):
    dual_graph = nx.MultiGraph()
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

            dual_graph.add_edge(right_face_node, left_face_node, edge=frozenset({v, w}))
    return dual_graph

  def cocircuit(self, X: frozenset) -> frozenset:
    visited = {node: False for node in self.dual_graph.nodes()}
    stack = []
    edge_dict = {frozenset({u, v}): False for u, v in X}

    def dfs(u, parent):
        print(f"Visiting: {u}")
        visited[u] = True
        stack.append(u)
        for v in self.dual_graph.neighbors(u):
            for k in self.dual_graph[u][v]:
                edge_uv = frozenset({u, v})
                if edge_uv in edge_dict and not edge_dict[edge_uv]:
                    edge_dict[edge_uv] = True
                    print(f"Processing edge: {u}-{v}")
                    if v == parent:
                        continue
                    if visited[v]:
                        cycle_start = stack.index(v)
                        print(f"Cycle detected starting at: {v}")
                        return stack[cycle_start:]
                    else:
                        result = dfs(v, u)
                        if result:
                            return result
        stack.pop()
        print(f"Backtracking from: {u}")
        return None

    for node in self.dual_graph.nodes():
        if not visited[node]:
            print(f"Starting DFS from node: {node}")
            cycle = dfs(node, None)
            if cycle:
                cycle_edges = []
                for i in range(len(cycle)):
                    next_node = cycle[(i + 1) % len(cycle)]
                    edge_cycle = frozenset({cycle[i], next_node})
                    if edge_cycle in X:
                        cycle_edges.append((cycle[i], next_node))
                print(f"Cycle edges in X: {cycle_edges}")
                return frozenset(cycle_edges)
    print("No cycle found")
    return frozenset()


  def delete(self, element):
    pass

  def contract(self, element):
    pass


edges = [(1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (2, 5), (4, 5)]
matroid = PlanarMatroid(edges)
print(matroid.dual_graph.edges(data=True))
# cocircuit = matroid.cocircuit(frozenset([(1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (2, 5), (4, 5)]))
# print(cocircuit)