from matroids.uniform_matroid import UniformMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

groundset = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
k = 4
matroid = UniformMatroid(groundset, k)

bidder_a = Bidder({1: 2, 2: 4}, 'a')
bidder_b = Bidder({3: 2, 4: 3}, 'b')
bidder_c = Bidder({5: 1, 6: 23}, 'c')
bidder_d = Bidder({7: 7, 8: 7}, 'd')
bidder_e = Bidder({9: 24, 10: 6}, 'e')

base = unit_step_auction(matroid, [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e])
print(base)