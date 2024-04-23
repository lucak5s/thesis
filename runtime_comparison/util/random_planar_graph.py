import random
import networkx as nx

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