from matroid.linear_matroid import LinearMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction
import sympy as sp

def test_unit_step_auction_1():
  array = [
    [1, 0, 0, 0, 0, 1, 1, -1],
    [0, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, -1, 1, 1, 0]
  ]
  matrix = sp.Matrix(array)
  matroid = LinearMatroid(matrix)

  bidder_a = Bidder({0: 2}, 'a')
  bidder_b = Bidder({1: 6}, 'b')
  bidder_c = Bidder({2: 9}, 'c')
  bidder_d = Bidder({3: 1}, 'd')
  bidder_e = Bidder({4: 11}, 'e')
  bidder_f = Bidder({5: 5}, 'f')
  bidder_g = Bidder({6: 13}, 'g')
  bidder_h = Bidder({7: 3}, 'h')
  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f, bidder_g, bidder_h]

  base = unit_step_auction(matroid, bidders)
  assert base == frozenset({1, 2, 4, 6})

def test_unit_step_auction_2():
  array = [
    [1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 1]
  ]
  matrix = sp.Matrix(array)
  matroid = LinearMatroid(matrix)

  bidder_a = Bidder({0: 2}, 'a')
  bidder_b = Bidder({1: 6}, 'b')
  bidder_c = Bidder({2: 9}, 'c')
  bidder_d = Bidder({3: 1}, 'd')
  bidder_e = Bidder({4: 11}, 'e')
  bidder_f = Bidder({5: 5}, 'f')
  bidder_g = Bidder({6: 13}, 'g')
  bidder_h = Bidder({7: 3}, 'h')
  bidder_i = Bidder({8: 1}, 'i')
  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f, bidder_g, bidder_h, bidder_i]

  base = unit_step_auction(matroid, bidders)
  assert base == frozenset({2, 4, 5, 6, 7})
  
def test_unit_step_auction_3():
  edges = [frozenset({1, 2}), frozenset({1, 3}), frozenset({2, 3}), frozenset({3, 4}), frozenset({2, 4})]

  bidder_a = Bidder({0: 5, 3: 4}, 'a')
  bidder_b = Bidder({1: 2, 4: 3}, 'b')
  bidder_c = Bidder({2: 1}, 'c')
  bidders = [bidder_a, bidder_b, bidder_c]

  incidence_array = [
      [1, 1, 0, 0, 0],
      [-1, 0, 1, 0, 1],
      [0, -1, -1, 1, 0],
      [0, 0, 0, -1, -1]
  ]

  incidence_matrix = sp.Matrix(incidence_array)
  linear_matroid = LinearMatroid(incidence_matrix)
  base = unit_step_auction(linear_matroid, bidders)
  assert base == frozenset({0, 3, 4})
  
# def test_unit_step_auction_4():
#   array = [
#     [1, 1, 0, 0, 1, -1],
#     [-1, -1, -1, 0, 0, 0],
#     [0, 0, 0, 0, -1, 0],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0]
#   ]
#   weighted_edges = [(frozenset({8, 2}), 472), (frozenset({1, 4}), 636), (frozenset({9, 3}), 756), (frozenset({2, 6}), 239), (frozenset({4, 5}), 805), (frozenset({8, 7}), 378), (frozenset({9, 4}), 195), (frozenset({3, 4}), 989), (frozenset({0, 6}), 221), (frozenset({0, 2}), 689), (frozenset({0, 4}), 193), (frozenset({2, 4}), 227), (frozenset({8, 1}), 291), (frozenset({1, 6}), 68), (frozenset({8, 5}), 828), (frozenset({1, 3}), 68), (frozenset({4, 7}), 457), (frozenset({0, 1}), 902), (frozenset({1, 5}), 800), (frozenset({8, 6}), 970), (frozenset({2, 7}), 692), (frozenset({0, 9}), 517), (frozenset({1, 9}), 880), (frozenset({8, 4}), 862)]
#   index_edge_map = {index: edge for index, (edge, weight) in enumerate(weighted_edges)}
#   bidders = [Bidder({index: weight}, str(edge)) for index, (edge, weight) in enumerate(weighted_edges)]

#   incidence_matrix = sp.Matrix(array)
#   linear_matroid = LinearMatroid(incidence_matrix)
#   base = unit_step_auction(linear_matroid, bidders)
#   base_in_edges = frozenset([index_edge_map[index] for index in base])
  
#   correct_base = frozenset({frozenset({3, 4}), frozenset({1, 9}), frozenset({0, 1}), frozenset({0, 2}), frozenset({8, 6}), frozenset({1, 5}), frozenset({8, 5}), frozenset({2, 7}), frozenset({8, 4})})
#   assert base_in_edges == correct_base

  