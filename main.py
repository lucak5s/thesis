import networkx as nx

def build_dual_graph(embedding):
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

            dual_graph.add_edge(right_face_node, left_face_node, color=f'({v}, {w})')
    return dual_graph

G = nx.Graph([(1, 2), (2, 3), (3, 1), (3, 4), (2, 4)])

is_planar, embedding = nx.check_planarity(G)
if is_planar:
    dual_graph = build_dual_graph(embedding)
else:
    print("The graph is not planar and cannot have a dual graph.")
