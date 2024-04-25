from auction.bidder import Bidder
from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from matroid.linear_matroid import LinearMatroid
import random
import sympy as sp
from runtime_comparison.util.random_planar_graph import random_planar_graph
from runtime_comparison.util.vertex_edge_incidence_matrix import vertex_edge_incidence_matrix
from runtime_comparison.util.timed_unit_step_auction import timed_unit_step_auction

def planar_graphic_linear_comparison(amounts_of_nodes, density_type):
  linear_runtimes = []
  graphic_runtimes = []
  planar_runtimes = []
  
  for amount_of_nodes in amounts_of_nodes:
    
    ### Random Input ###
    
    G = random_planar_graph(amount_of_nodes, density_type)
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
    
    linear_base, linear_runtime = timed_unit_step_auction(linear_matroid, linear_bidders)
    linear_base_in_edges = frozenset([index_edge_map[index] for index in linear_base])
    
    linear_runtimes.append(linear_runtime)

    ## Graphic Matroid ###

    graphic_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
    graphic_matroid = GraphicMatroid(vertices, edges)
    
    graphic_base, graphic_runtime = timed_unit_step_auction(graphic_matroid, graphic_bidders)
    
    graphic_runtimes.append(graphic_runtime)

    ### Planar Matroid ###

    planar_bidders = [Bidder({edge: weight}, str(edge)) for edge, weight in weighted_edges]
    planar_matroid = PlanarMatroid(edges)
    
    planar_base, planar_runtime = timed_unit_step_auction(planar_matroid, planar_bidders)
    
    planar_runtimes.append(planar_runtime)
    
  return {
    'linear_runtimes': linear_runtimes,
    'graphic_runtimes': graphic_runtimes,
    'planar_runtimes': planar_runtimes
  }
