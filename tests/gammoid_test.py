from matroids.gammoid import Gammoid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

def test_unit_step_auction():
  vertices = frozenset({
    'a', 'b', 'c', 'd', 'e', 'f', 'g'
  })
  edges = frozenset({
    ('a', 'c'),
    ('b', 'g'),
    ('b', 'd'),
    ('c', 'e'),
    ('e', 'd'),
    ('e', 'f')
  })
  sources = frozenset({
    'a', 'b', 'c', 'e'
  })
  sinks = frozenset({
    'g', 'c', 'd', 'e'
  })

  matroid = Gammoid(vertices, edges, sources, sinks)

  bidder_a = Bidder({'d': 12}, 'a')
  bidder_b = Bidder({'g': 25}, 'b')
  bidder_c = Bidder({'c': 24}, 'c')
  bidder_d = Bidder({'e': 11}, 'd')

  bidders = [bidder_a, bidder_b, bidder_c, bidder_d]

  base = unit_step_auction(matroid, bidders)

  assert base == frozenset({'d', 'g', 'c'})




