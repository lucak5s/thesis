from matroids.scheduling_matroid import SchedulingMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

deadlines = { 'g': 5, 'h': 5, 'i': 5, 'f': 3, 'e': 3, 'c': 2, 'd': 2, 'a': 1, 'b': 1 }

matroid = SchedulingMatroid(deadlines, 1)

bidder_a = Bidder({'a': 2}, 'a')
bidder_b = Bidder({'b': 1}, 'b')
bidder_c = Bidder({'c': 24}, 'c')
bidder_d = Bidder({'d': 6}, 'd')
bidder_e = Bidder({'e': 2}, 'e')
bidder_f = Bidder({'f': 6}, 'f')
bidder_g = Bidder({'g': 30}, 'g')
bidder_h = Bidder({'h': 35}, 'h')


base = unit_step_auction(matroid, [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f, bidder_g, bidder_h])
print(base)