import pytest
from matroids.graphic_matroid import GraphicMatroid
from auction.bidder import Bidder
from auction.unit_step_auction import unit_step_auction

@pytest.fixture
def main_paper_example():
  vertices = frozenset({1, 2, 3, 4})
  edges = frozenset({frozenset({1, 2}), frozenset({1, 4}), frozenset({2, 4}), frozenset({3, 4}), frozenset({2, 3})})
  matroid = GraphicMatroid(vertices, edges)

  bidder_a = Bidder({frozenset({1, 2}): 5, frozenset({3, 4}): 4}, 'a')
  bidder_b = Bidder({frozenset({1, 4}): 2, frozenset({2, 3}): 3}, 'b')
  bidder_c = Bidder({frozenset({2, 4}): 1}, 'c')
  bidders = [bidder_a, bidder_b, bidder_c]

  return (matroid, bidders)

def test_unit_step_auction(main_paper_example):
    matroid, bidders = main_paper_example
    base = unit_step_auction(matroid, bidders)
    assert base == frozenset({frozenset({3, 4}), frozenset({2, 3}), frozenset({1, 2})})

