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

  bidder_a = Bidder({'a': 12, 'b': 25}, 'a')
  bidder_b = Bidder({'c': 24}, 'b')
  bidder_c = Bidder({'d': 11, 'e': 33}, 'c')
  bidder_d = Bidder({'f': 1}, 'd')

  bidders = [bidder_a, bidder_b, bidder_c, bidder_d]

  base = unit_step_auction(matroid, bidders)

  assert base == frozenset({'b', 'c', 'e'})


def test_large_uniform_matroid():
  vertices = frozenset({
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  })

  
  starting_vertices = frozenset({
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
  })
  destination_vertices = frozenset({
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  })
  
  edges = []
  for u in starting_vertices:
    for v in destination_vertices:
      edges.append((u, v))

  matroid = Gammoid(vertices, edges, starting_vertices, destination_vertices)

  bidder_a = Bidder({'a': 12, 'b': 25, 'c': 24}, 'a')
  bidder_b = Bidder({'d': 13, 'e': 33}, 'b')
  bidder_c = Bidder({'f': 11, 'g': 15, 'h': 33, 'i': 88}, 'c')
  bidder_d = Bidder({'j': 6, 'k': 33, 'l': 22, 'm': 18}, 'd')
  bidder_e = Bidder({'n': 63, 'o': 21, 'p': 43, 'q': 13}, 'e')

  bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e]

  base = unit_step_auction(matroid, bidders)
  
  assert base == frozenset({'b', 'c', 'e', 'h', 'i', 'k', 'n', 'p', 'l'})


