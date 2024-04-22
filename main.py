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

def random_planar_graph(num_nodes, attempts=1000):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for _ in range(attempts):
        u, v = random.sample(G.nodes, 2)
        add_edge_if_planar(G, u, v)
    return G

num_nodes = 20
num_attempts = 300
G = random_planar_graph(num_nodes, num_attempts)

vertices = frozenset(G.nodes())
edges = frozenset([frozenset(edge) for edge in G.edges()])
weighted_edges = [(edge, random.randint(1, 100)) for edge in edges]

###

graphic_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, graphic_bidders)
print('base:', graphic_base)

###

planar_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, planar_bidders)
print('base:', planar_base)

### 

def vertex_edge_incidence_matrix(vertices, edges):
    num_vertices = len(vertices)
    num_edges = len(edges)
    vertex_edge_matrix = np.zeros((num_vertices, num_edges))

    node_index_map = {node: i for i, node in enumerate(vertices)}

    for i, edge in enumerate(edges):
        u, v = tuple(edge)
        vertex_edge_matrix[node_index_map[u], i] = 1
        vertex_edge_matrix[node_index_map[v], i] = -1

    return vertex_edge_matrix

linear_bidders = [Bidder({index: weight}, str(edge)) for index, (edge, weight) in enumerate(weighted_edges)]
incidence_matrix = vertex_edge_incidence_matrix(list(vertices), [edge for edge, weight in weighted_edges])
matrix = sp.Matrix(incidence_matrix)
linear_matroid = LinearMatroid(matrix)
linear_base = unit_step_auction(linear_matroid, linear_bidders)
print('base:', linear_base)