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
    for node in G.nodes():
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

def random_planar_graph(num_nodes, density_type='sparse'):
    if density_type == 'sparse':
        edge_target = num_nodes  
    elif density_type == 'semi-dense':
        edge_target = 2 * num_nodes
    elif density_type == 'dense':
        edge_target = 3 * num_nodes - 6 

    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    while G.number_of_edges() < edge_target:
        u, v = random.sample(list(G.nodes()), 2)
        if u != v:
            add_edge_if_planar(G, u, v)

    if ensure_two_connected(G):
        return G
    else:
        return None