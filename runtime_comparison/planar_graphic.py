from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction
import copy
  
vertices = frozenset({1, 2, 3, 4})
edges = frozenset({frozenset({1, 2}), frozenset({1, 4}), frozenset({2, 4}), frozenset({3, 4}), frozenset({2, 3})})

bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
bidders = [bidder_a, bidder_b, bidder_c]

graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, bidders)
print('base:', graphic_base)

####

bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
bidders = [bidder_a, bidder_b, bidder_c]

planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, bidders)
print('base:', planar_base)

###
###
###

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

bidder_a = Bidder({frozenset({'a', 'd'}): 1, frozenset({'b', 'f'}): 5, frozenset({'c', 'k'}): 7, frozenset({'k', 'j'}): 12}, 'a')
bidder_b = Bidder({frozenset({'d', 'h'}): 14, frozenset({'a', 'b'}): 4, frozenset({'f', 'g'}): 6}, 'b')
bidder_c = Bidder({frozenset({'d', 'e'}): 3, frozenset({'e', 'f'}): 11, frozenset({'c', 'g'}): 8}, 'c')
bidder_d = Bidder({frozenset({'h', 'i'}): 15, frozenset({'i', 'j'}): 16, frozenset({'g', 'k'}): 9, frozenset({'b', 'c'}): 10}, 'd')
bidder_e = Bidder({frozenset({'a', 'e'}): 2, frozenset({'e', 'h'}): 18, frozenset({'f', 'i'}): 13, frozenset({'g', 'j'}): 17}, 'd')
bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e]

graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, bidders)
print('base:', graphic_base)

###

bidder_a = Bidder({frozenset({'a', 'd'}): 1, frozenset({'b', 'f'}): 5, frozenset({'c', 'k'}): 7, frozenset({'k', 'j'}): 12}, 'a')
bidder_b = Bidder({frozenset({'d', 'h'}): 14, frozenset({'a', 'b'}): 4, frozenset({'f', 'g'}): 6}, 'b')
bidder_c = Bidder({frozenset({'d', 'e'}): 3, frozenset({'e', 'f'}): 11, frozenset({'c', 'g'}): 8}, 'c')
bidder_d = Bidder({frozenset({'h', 'i'}): 15, frozenset({'i', 'j'}): 16, frozenset({'g', 'k'}): 9, frozenset({'b', 'c'}): 10}, 'd')
bidder_e = Bidder({frozenset({'a', 'e'}): 2, frozenset({'e', 'h'}): 18, frozenset({'f', 'i'}): 13, frozenset({'g', 'j'}): 17}, 'd')
bidders = [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e]

planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, bidders)
print('base:', planar_base)

###
###
###

vertices = frozenset([x for x in range(50)])
edges_list = [(0, 14), (0, 34), (1, 16), (1, 34), (1, 11), (1, 5), (1, 4), (1, 30), (1, 37), (1, 28), (2, 14), (2, 6), (3, 40), (3, 9), (3, 12), (3, 47), (3, 38), (3, 24), (3, 43), (4, 10), (4, 20), (4, 43), (4, 30), (4, 35), (4, 6), (5, 32), (5, 21), (6, 14), (6, 38), (7, 38), (7, 41), (7, 44), (7, 46), (7, 23), (7, 30), (8, 22), (8, 44), (8, 29), (9, 17), (9, 38), (10, 30), (10, 18), (10, 19), (10, 39), (10, 33), (10, 15), (10, 20), (11, 20), (12, 47), (12, 40), (13, 43), (13, 35), (13, 38), (14, 34), (15, 31), (15, 48), (15, 33), (16, 38), (16, 34), (16, 30), (17, 24), (18, 26), (18, 48), (19, 32), (19, 20), (20, 32), (21, 28), (21, 37), (21, 32), (22, 23), (22, 41), (23, 43), (23, 30), (24, 46), (25, 45), (25, 36), (26, 45), (27, 40), (27, 47), (28, 37), (28, 32), (29, 47), (29, 40), (29, 43), (30, 42), (30, 45), (30, 33), (31, 45), (31, 42), (31, 36), (32, 45), (33, 42), (34, 49), (35, 38), (36, 48), (38, 49), (40, 43), (41, 44), (44, 47)]
edges = frozenset([frozenset(edge) for edge in edges_list])

bidders_graphic = [{edge: random.randint(1, 100)} for edge in edges]
bidders_planar = copy.deepcopy(bidders_graphic)

graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, bidders_graphic)
print('base:', graphic_base)

###

planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, bidders_planar)
print('base:', planar_base)