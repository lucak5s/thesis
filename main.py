from matroids.matroid import BasesMatroid
from auctions.bidder import Bidder
from auctions.unit_step_auction import unit_step_auction

groundset = frozenset(['a:5', 'b:2', 'b:3', 'a:4', 'c:1'])

bases = frozenset([
  frozenset(['a:5', 'c:1', 'a:4']),
  frozenset(['a:5', 'c:1', 'b:3']),
  frozenset(['a:5', 'b:3', 'a:4']),
  frozenset(['a:5', 'b:2', 'a:4']),
  frozenset(['a:5', 'b:2', 'b:3']),
  frozenset(['b:2', 'a:4', 'b:3']),
  frozenset(['b:2', 'c:1', 'b:3']),
  frozenset(['b:2', 'c:1', 'a:4']),
])

matroid = BasesMatroid(groundset, bases)

bidder_a = Bidder({'a:5': 5, 'a:4': 4}, 'a')
bidder_b = Bidder({'b:2': 2, 'b:3': 3}, 'b')
bidder_c = Bidder({'c:1': 1}, 'c')

base = unit_step_auction(matroid, [bidder_a, bidder_b, bidder_c])
print(base)