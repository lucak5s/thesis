from matroid.gammoid import Gammoid
from auction.bidder import Bidder
from auction.auction import unit_step_auction

def test_uniform_matroid():
  vertices = frozenset({
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
  })

  
  starting_vertices = frozenset({
    'a', 'b', 'c', 'd', 'e', 'f'
  })
  destination_vertices = frozenset({
    'g', 'h', 'i'
  })
  
  edges = []
  for u in starting_vertices:
    for v in destination_vertices:
      edges.append((u, v))

  matroid = Gammoid(vertices, edges, starting_vertices, destination_vertices)

  bidder_a = Bidder({'a': 12}, 'a')
  bidder_b = Bidder({'b': 25}, 'b')
  bidder_c = Bidder({'c': 24}, 'c')
  bidder_d = Bidder({'d': 11}, 'd')
  bidder_e = Bidder({'e': 33}, 'e')
  bidder_f = Bidder({'f': 1}, 'f')

  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f]

  base = unit_step_auction(matroid, bidders)

  assert base == frozenset({'b', 'c', 'e'})




