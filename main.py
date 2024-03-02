from matroids.gammoid import Gammoid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

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
  'a', 'b'
})
sinks = frozenset({
  'g', 'c', 'd'
})

matroid = Gammoid(vertices, edges, sources, sinks)

bidder_a = Bidder({'d': 5}, 'a')
bidder_b = Bidder({'g': 1}, 'b')
bidder_c = Bidder({'c': 24}, 'c')

bidders = [bidder_a, bidder_b, bidder_c]
print(matroid.full_rank())
base = unit_step_auction(matroid, bidders)


