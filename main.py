from matroids.graphic_matroid import GraphicMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

vertices = frozenset({1, 2, 3, 4})
edges = frozenset({
  frozenset({1, 2}),
  frozenset({1, 4}),
  frozenset({2, 4}),
  frozenset({3, 4}),
  frozenset({2, 3}),
})

matroid = GraphicMatroid(vertices, edges)

bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')

base = unit_step_auction(matroid, [bidder_a, bidder_b, bidder_c])
print(base)