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

def random_planar_graph(num_edges, density_type='sparse'):
    if density_type == 'sparse':
        node_target = num_edges  
    elif density_type == 'semi-dense':
        node_target = num_edges // 2 + 1
    elif density_type == 'dense':
        node_target = num_edges // 3 + 6
    
    G = nx.Graph()
    G.add_nodes_from(range(node_target))
    
    for i in range(node_target):
        G.add_edge(i, (i + 1) % node_target)

    ensure_two_connected(G)
    
    while G.number_of_edges() < num_edges:
        u, v = random.sample(list(G.nodes()), 2)
        if u != v:
            add_edge_if_planar(G, u, v)
    
    return G