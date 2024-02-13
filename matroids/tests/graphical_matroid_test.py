import pytest
from ..graphical_matroid import GraphicalMatroid

@pytest.fixture
def shared_matroid():
    vertices = frozenset(
      ['a', 'b', 'c', 'd']
    )
    edges = frozenset([
      frozenset(['a', 'b']),
      frozenset(['b', 'd']),
      frozenset(['a', 'd']),
      frozenset(['b', 'c']),
      frozenset(['d', 'c']),
    ])
    matroid = GraphicalMatroid(vertices, edges)
    return matroid

def test_cocircuit(shared_matroid):
    cocircuit = shared_matroid.cocircuit(frozenset([
      frozenset(['a', 'd']),
      frozenset(['b', 'c'])
    ]))
    assert cocircuit == frozenset()

    cocircuit = shared_matroid.cocircuit(frozenset([
      frozenset(['a', 'd']),
      frozenset(['a', 'b']),
      frozenset(['d', 'b'])
    ]))
    assert cocircuit == frozenset([
      frozenset(['a', 'd']),
      frozenset(['a', 'b'])
    ])

def test_contract(shared_matroid):
    shared_matroid.contract(frozenset([
      frozenset(['a', 'b'])
    ]))
    assert 1 == 1

def test_delete(shared_matroid):
    shared_matroid.delete(frozenset([
        frozenset(['a', 'b'])
    ]))
    assert frozenset(['a', 'b']) not in shared_matroid.edges