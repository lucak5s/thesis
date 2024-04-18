from matroid.linear_matroid import LinearMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction

def test_unit_step_auction_1():
  columns = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 1, -1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [-1, 1, 1, 0]
  ]
  matroid = LinearMatroid(columns)

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
  columns = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
  ]
  matroid = LinearMatroid(columns)

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