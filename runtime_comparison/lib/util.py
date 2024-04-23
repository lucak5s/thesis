import networkx as nx
import numpy as np
import random

def add_edge_if_planar(G, u, v):
    G.add_edge(u, v)
    planar, _ = nx.check_planarity(G)
    if not planar:
        G.remove_edge(u, v)
        return False
    return True

def ensure_two_connected(G):
    for node in list(G.nodes()):
        if G.degree[node] < 2:
            neighbors = list(G.nodes())
            random.shuffle(neighbors)
            added_edges = 0
            for neighbor in neighbors:
                if neighbor != node and G.degree[neighbor] < len(G) - 1:
                    if add_edge_if_planar(G, node, neighbor):
                        added_edges += 1
                        if added_edges == 2:
                            break
            if added_edges < 2:
                return False  
    return True

def random_planar_graph(num_nodes, attempts=1000):
    attempts = max(num_nodes * 2, attempts)
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for _ in range(attempts):
        u, v = random.sample(list(G.nodes()), 2)
        add_edge_if_planar(G, u, v)
    if ensure_two_connected(G):
        return G
    else:
        return None
    
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