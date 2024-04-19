from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction
  
vertices = frozenset({1, 2, 3, 4})
edges = frozenset({frozenset({1, 2}), frozenset({1, 4}), frozenset({2, 4}), frozenset({3, 4}), frozenset({2, 3})})

bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
bidders = [bidder_a, bidder_b, bidder_c]

graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, bidders)
print('base:', graphic_base)


#####


bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
bidders = [bidder_a, bidder_b, bidder_c]

planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, bidders)
print('base:', planar_base)