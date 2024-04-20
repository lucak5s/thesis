from matroid.planar_matroid import PlanarMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction

def test_main_paper_example():
  vertices = frozenset({1, 2, 3, 4})
  edges = frozenset({frozenset({1, 2}), frozenset({1, 4}), frozenset({2, 4}), frozenset({3, 4}), frozenset({2, 3})})
  matroid = PlanarMatroid(edges)

  bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
  bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
  bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
  bidders = [bidder_a, bidder_b, bidder_c]

  base = unit_step_auction(matroid, bidders)
  assert base == frozenset({frozenset({3, 4}), frozenset({2, 3}), frozenset({1, 2})})

def test_large_graph():
  vertices = frozenset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'})
  edges = frozenset({
    frozenset({'a', 'd'}), 
    frozenset({'a', 'e'}),
    frozenset({'a', 'b'}),
    frozenset({'b', 'f'}),
    frozenset({'b', 'c'}),
    frozenset({'c', 'g'}),
    frozenset({'c', 'k'}),
    frozenset({'d', 'h'}),
    frozenset({'d', 'e'}),
    frozenset({'e', 'h'}),
    frozenset({'e', 'f'}),
    frozenset({'f', 'i'}),
    frozenset({'f', 'g'}),
    frozenset({'g', 'j'}),
    frozenset({'g', 'k'}),
    frozenset({'k', 'j'}),
    frozenset({'h', 'i'}),
    frozenset({'i', 'j'}),               
  })
  matroid = PlanarMatroid(edges)

  bidder_a = Bidder({frozenset({'a', 'd'}): 1, frozenset({'b', 'f'}): 5, frozenset({'c', 'k'}): 7, frozenset({'k', 'j'}): 12}, 'a')
  bidder_b = Bidder({frozenset({'d', 'h'}): 14, frozenset({'a', 'b'}): 4, frozenset({'f', 'g'}): 6}, 'b')
  bidder_c = Bidder({frozenset({'d', 'e'}): 3, frozenset({'e', 'f'}): 11, frozenset({'c', 'g'}): 8}, 'c')
  bidder_d = Bidder({frozenset({'h', 'i'}): 15, frozenset({'i', 'j'}): 16, frozenset({'g', 'k'}): 9, frozenset({'b', 'c'}): 10}, 'd')
  bidder_e = Bidder({frozenset({'a', 'e'}): 2, frozenset({'e', 'h'}): 18, frozenset({'f', 'i'}): 13, frozenset({'g', 'j'}): 17}, 'd')
  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e]

  base = unit_step_auction(matroid, bidders)
  assert base == frozenset({
    frozenset({'i', 'h'}), 
    frozenset({'b', 'c'}), 
    frozenset({'h', 'd'}), 
    frozenset({'i', 'j'}), 
    frozenset({'j', 'k'}), 
    frozenset({'a', 'b'}), 
    frozenset({'h', 'e'}), 
    frozenset({'g', 'c'}), 
    frozenset({'i', 'f'}), 
    frozenset({'j', 'g'})
  })
