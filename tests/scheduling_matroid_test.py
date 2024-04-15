from matroids.scheduling_matroid import SchedulingMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

def test_unit_step_auction():
  deadlines_1 = {
    1: set({'g', 'h', 'i'}),
    2: set({'e', 'f'}),
    3: set({'c', 'd'}),
    4: set({'a', 'b'})
  }

  # deadlines_2 = {
  #   5: set({'g', 'h', 'i'}),
  #   3: set({'e', 'f'}),
  #   2: set({'c', 'd'}),
  #   1: set({'a', 'b'})
  # }

  # deadlines_3 = {
  #   1: set({'a'}),
  #   3: set({'b', 'c', 'd', 'e'}),
  # }

  # deadlines_4 = {
  #   2: set({'a', 'b', 'c', 'd', 'e'}),
  # }

  matroid = SchedulingMatroid(deadlines_1)

  bidder_a = Bidder({'a': 2}, 'a')
  bidder_b = Bidder({'b': 1}, 'b')
  bidder_c = Bidder({'c': 24}, 'c')
  bidder_d = Bidder({'d': 7}, 'd')
  bidder_e = Bidder({'e': 2}, 'e')
  bidder_f = Bidder({'f': 6}, 'f')
  bidder_g = Bidder({'g': 30}, 'g')
  bidder_h = Bidder({'h': 35}, 'h')
  bidder_i = Bidder({'i': 1}, 'i')

  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f, bidder_g, bidder_h, bidder_i]

  base = unit_step_auction(matroid, bidders)

  assert base == frozenset({'h', 'd', 'g', 'c', 'f'})

  
