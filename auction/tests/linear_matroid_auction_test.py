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

  