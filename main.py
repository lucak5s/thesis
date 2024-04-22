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

bidders_graphic = [Bidder({edge: random.randint(1, 100)}, str(edge)) for edge in edges]
bidders_planar = copy.deepcopy(bidders_graphic)
bidders_linear = copy.deepcopy(bidders_graphic)

# graphic_matroid = GraphicMatroid(vertices, edges)
# graphic_base = unit_step_auction(graphic_matroid, bidders_graphic)
# print('base:', graphic_base)

# ###

# planar_matroid = PlanarMatroid(edges)
# planar_base = unit_step_auction(planar_matroid, bidders_planar)
# print('base:', planar_base)



### 

def vertex_edge_incidence_matrix(G):
    num_vertices = len(G.nodes)
    num_edges = len(G.edges)
    vertex_edge_matrix = np.zeros((num_vertices, num_edges))

    node_index_map = {node: i for i, node in enumerate(G.nodes)}

    for i, (u, v, key) in enumerate(G.edges(keys=True)):
        vertex_edge_matrix[node_index_map[u], i] = 1
        vertex_edge_matrix[node_index_map[v], i] = -1

    return vertex_edge_matrix

np_array = nx.to_numpy_array(G)
matrix = sp.Matrix(np_array)
linear_matroid = LinearMatroid(matrix)
print(linear_matroid.dual_matrix)
linear_base = unit_step_auction(linear_matroid, bidders_linear)
print('base:', linear_base)


print(planar_base == graphic_base)
print(planar_base == linear_base)
