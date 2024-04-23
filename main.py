from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from matroid.linear_matroid import LinearMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction
import networkx as nx
import random
import copy
import numpy as np
import sympy as sp

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
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for _ in range(attempts):
        u, v = random.sample(list(G.nodes()), 2)
        add_edge_if_planar(G, u, v)
    if ensure_two_connected(G):
        return G
    else:
        return None

num_nodes = 200
G = random_planar_graph(num_nodes)

vertices = frozenset(G.nodes())
edges = frozenset([frozenset(edge) for edge in G.edges()])
weighted_edges = [(edge, random.randint(1, 1000)) for edge in edges]

### Linear Matroid ###

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

linear_bidders = [Bidder({index: weight}, str(edge)) for index, (edge, weight) in enumerate(weighted_edges)]
index_edge_map = {index: edge for index, (edge, weight) in enumerate(weighted_edges)}
incidence_matrix = vertex_edge_incidence_matrix(list(vertices), [edge for edge, weight in weighted_edges])
matrix = sp.Matrix(incidence_matrix)
matrix = matrix.applyfunc(lambda x: int(x))
linear_matroid = LinearMatroid(matrix)
linear_base = unit_step_auction(linear_matroid, linear_bidders)
linear_base_in_edges = frozenset([index_edge_map[index] for index in linear_base])

### Max Weight Basis ###

weighted_indices = [(index, weight) for index, (edge, weight) in enumerate(weighted_edges)]
sorted_edges = sorted(weighted_indices, reverse=True, key=lambda x: x[1])
base = []

matrix = LinearMatroid(matrix).dual_matrix
matrix = LinearMatroid(matrix).dual_matrix
for index, _ in sorted_edges:
    curr_matrix = matrix[:, base + [index]]
    rref_matrix = curr_matrix.rref()
    if len(rref_matrix[1]) == curr_matrix.cols: base.append(index)

base_in_edges = frozenset([index_edge_map[index] for index in base])
print(base_in_edges)

## Graphic Matroid ###

graphic_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, graphic_bidders)

### Planar Matroid ###

planar_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, planar_bidders)

### Correctness ###

print('graphic-planar', graphic_base == planar_base)
print('graphic-greedy', graphic_base == base_in_edges)
print('graphic-linear', graphic_base == linear_base_in_edges)