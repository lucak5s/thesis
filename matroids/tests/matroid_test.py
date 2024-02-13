import pytest
from ..matroid import Matroid

@pytest.fixture
def shared_matroid():
    groundset = frozenset([1, 2, 3, 4])
    independent_sets = frozenset([
      frozenset([1, 2]),
      frozenset([1, 3]),
      frozenset([1]),
      frozenset([2]),
      frozenset([3]),
      frozenset()
    ])
    matroid = Matroid(groundset, independent_sets)
    return matroid

def test_independence_oracle(shared_matroid):
    assert shared_matroid.independence_oracle(frozenset({1, 2}))
    assert not shared_matroid.independence_oracle(frozenset({2, 3}))

def test_cocircuit(shared_matroid):
    cocircuit = shared_matroid.cocircuit(frozenset({1, 2}))
    assert cocircuit == frozenset({1})

    cocircuit = shared_matroid.cocircuit(frozenset({2, 3}))
    assert cocircuit == frozenset({2, 3})

def test_contract(shared_matroid):
    shared_matroid.contract(frozenset({4}))
    assert shared_matroid.independence_oracle(frozenset({3}))

def test_delete(shared_matroid):
    shared_matroid.delete(frozenset([1]))
    assert 1 not in shared_matroid.groundset