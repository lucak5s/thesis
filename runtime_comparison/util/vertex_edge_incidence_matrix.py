import numpy as np
    
def vertex_edge_incidence_matrix(vertices, edges):
    num_vertices = len(vertices)
    num_edges = len(edges)
    vertex_edge_matrix = np.zeros((num_vertices, num_edges))

    node_index_map = {node: i for i, node in enumerate(vertices)}
    for i, edge in enumerate(edges):
        u, v = tuple(edge)
        if u == v: continue
        vertex_edge_matrix[node_index_map[u], i] = 1
        vertex_edge_matrix[node_index_map[v], i] = -1
        
    return vertex_edge_matrix