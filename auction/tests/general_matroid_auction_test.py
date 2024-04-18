import pytest
from matroid.general_matroid import GeneralMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction

@pytest.fixture
def main_paper_example():
  groundset = frozenset(['a:5', 'b:2', 'b:3', 'a:4', 'c:1'])
  independent_sets = frozenset({frozenset({'a:5'}), frozenset({'b:2', 'c:1', 'a:4'}), frozenset({'c:1', 'a:5', 'a:4'}), frozenset({'b:2', 'c:1', 'b:3'}), frozenset({'a:5', 'c:1'}), frozenset({'a:5', 'c:1', 'b:3'}), frozenset({'a:5', 'b:3'}), frozenset({'a:5', 'b:2'}), frozenset({'a:4', 'b:3'}), frozenset({'a:5', 'a:4'}), frozenset({'b:2', 'a:5', 'a:4'}), frozenset({'b:2', 'a:4', 'b:3'}), frozenset({'a:5', 'b:2', 'b:3'}), frozenset({'a:4'}), frozenset({'c:1', 'b:3'}), frozenset({'b:3'}), frozenset({'c:1', 'a:4'}), frozenset({'b:2'}), frozenset({'a:5', 'a:4', 'b:3'}), frozenset(), frozenset({'b:2', 'b:3'}), frozenset({'c:1'}), frozenset({'b:2', 'c:1'}), frozenset({'b:2', 'a:4'})})
  matroid = GeneralMatroid(groundset, independent_sets)

  bidder_a = Bidder({'a:5': 5, 'a:4': 4}, 'a')
  bidder_b = Bidder({'b:2': 2, 'b:3': 3}, 'b')
  bidder_c = Bidder({'c:1': 1}, 'c')
  bidders = [bidder_a, bidder_b, bidder_c]

  return (matroid, bidders)

def test_unit_step_auction(main_paper_example):
  matroid, bidders = main_paper_example
  base = unit_step_auction(matroid, bidders)
  assert base == frozenset({'a:4', 'b:3', 'a:5'})

