from matroids.partition_matroid import PartitionMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

groundset = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
partitions = [
  (frozenset({1, 2, 3, 4}), 2),
  (frozenset({5, 6, 7}), 2),
  (frozenset({8, 9, 10}), 2)
]
matroid = PartitionMatroid(groundset, partitions)

bidder_a = Bidder({1: 2}, 'a')
bidder_b = Bidder({2: 1}, 'b')
bidder_c = Bidder({3: 24}, 'c')
bidder_d = Bidder({4: 6}, 'd')
bidder_e = Bidder({5: 2}, 'e')
bidder_f = Bidder({6: 6}, 'f')
bidder_g = Bidder({7: 3}, 'g')
bidder_h = Bidder({8: 35}, 'h')
bidder_i = Bidder({9: 61}, 'i')
bidder_j = Bidder({10: 11}, 'j')


base = unit_step_auction(matroid, [bidder_a, bidder_b, bidder_c, bidder_d, bidder_e, bidder_f, bidder_g, bidder_h, bidder_i, bidder_j])
print(base)