import pytest
from matroid.partition_matroid import PartitionMatroid

def test_initialization():
    groundset = frozenset({1, 2, 3, 4, 5, 6})
    partitions = [
        (frozenset({1, 2}), 1),
        (frozenset({3, 4, 5}), 2)
    ]
    matroid = PartitionMatroid(groundset, partitions)
    assert matroid.groundset == groundset
    assert matroid.partitions == partitions

def test_cocircuit():
    matroid = PartitionMatroid(
        frozenset({1, 2, 3, 4, 5, 6}),
        [(frozenset({1, 2, 3}), 2), (frozenset({4, 5, 6}), 2)]
    )
    X = frozenset({1, 2, 3})
    cocircuit = matroid.cocircuit(X) 
    assert cocircuit == frozenset()

    Y = frozenset({1, 2})  
    cocircuit = matroid.cocircuit(Y)
    assert cocircuit == frozenset({1, 2})

def test_delete():
    matroid = PartitionMatroid(
        frozenset({1, 2, 3, 4}),
        [(frozenset({1, 2}), 1), (frozenset({3, 4}), 2)]
    )
    matroid.delete(1)
    assert matroid.groundset == frozenset({2, 3, 4})
    assert matroid.partitions == [(frozenset({2}), 1), (frozenset({3, 4}), 2)]

def test_contract():
    matroid = PartitionMatroid(
        frozenset({1, 2, 3, 4}),
        [(frozenset({1, 2}), 1), (frozenset({3, 4}), 2)]
    )
    matroid.contract(2)
    assert matroid.groundset == frozenset({1, 3, 4})
    assert matroid.partitions == [(frozenset({1}), 0), (frozenset({3, 4}), 2)]

def test_multiple_operations():
    matroid = PartitionMatroid(
        frozenset({1, 2, 3, 4, 5, 6}),
        [(frozenset({1, 2, 3}), 2), (frozenset({4, 5, 6}), 2)]
    )
    matroid.delete(1)
    matroid.contract(2)
    matroid.contract(4)
    assert matroid.groundset == frozenset({3, 5, 6})
    assert matroid.partitions == [(frozenset({3}), 1), (frozenset({5, 6}), 1)]
    cocircuit = matroid.cocircuit(frozenset({5, 6})) 
    assert cocircuit == frozenset({5, 6})