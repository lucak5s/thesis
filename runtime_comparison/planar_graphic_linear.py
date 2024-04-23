from auction.bidder import Bidder
from auction.auction import unit_step_auction
from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from matroid.linear_matroid import LinearMatroid
import random
import sympy as sp
from runtime_comparison.util.random_planar_graph import random_planar_graph
from runtime_comparison.util.vertex_edge_incidence_matrix import vertex_edge_incidence_matrix

G = random_planar_graph(100)
vertices = frozenset(G.nodes())
edges = frozenset([frozenset(edge) for edge in G.edges()])
weighted_edges = [(edge, random.randint(1, 1000)) for edge in edges]

### Linear Matroid ###

linear_bidders = [Bidder({index: weight}, str(edge)) for index, (edge, weight) in enumerate(weighted_edges)]
index_edge_map = {index: edge for index, (edge, weight) in enumerate(weighted_edges)}
incidence_matrix = vertex_edge_incidence_matrix(list(vertices), [edge for edge, weight in weighted_edges])
matrix = sp.Matrix(incidence_matrix)
matrix = matrix.applyfunc(lambda x: int(x))
linear_matroid = LinearMatroid(matrix)
linear_base = unit_step_auction(linear_matroid, linear_bidders)
linear_base_in_edges = frozenset([index_edge_map[index] for index in linear_base])

## Graphic Matroid ###

graphic_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, graphic_bidders)

### Planar Matroid ###

planar_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, planar_bidders)

### Correctness ###

print('is correct:', planar_base == graphic_base == linear_base_in_edges)