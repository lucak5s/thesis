import pytest
from matroid.uniform_matroid import UniformMatroid

def test_initialization():
    groundset = frozenset({1, 2, 3})
    k = 2
    matroid = UniformMatroid(groundset, k)
    assert matroid.groundset == groundset
    assert matroid.k == k

def test_unique_cocircuit_correct_length():
    matroid = UniformMatroid(frozenset({1, 2, 3, 4}), 2)
    X = frozenset({1, 2})
    expected_cocircuit = frozenset()  
    assert matroid.cocircuit(X) == expected_cocircuit

def test_unique_cocircuit_incorrect_length():
    matroid = UniformMatroid(frozenset({1, 2, 3, 4}), 2)
    X = frozenset({1, 2, 3})
    expected_cocircuit = frozenset({1, 2, 3})  
    assert matroid.cocircuit(X) == expected_cocircuit

def test_contract():
    matroid = UniformMatroid(frozenset({1, 2, 3}), 2)
    matroid.contract(1)
    assert matroid.groundset == frozenset({2, 3})
    assert matroid.k == 1

def test_delete():
    matroid = UniformMatroid(frozenset({1, 2, 3}), 2)
    matroid.delete(1)
    assert matroid.groundset == frozenset({2, 3})
    assert matroid.k == 2  

def test_multiple_operations():
    matroid = UniformMatroid(frozenset({1, 2, 3, 4}), 3)
    matroid.delete(1)
    assert matroid.groundset == frozenset({2, 3, 4})
    assert matroid.k == 3
    matroid.contract(2)
    assert matroid.groundset == frozenset({3, 4})
    assert matroid.k == 2
    cocircuit = matroid.cocircuit(frozenset({3}))
    assert cocircuit == frozenset({3}) 

def test_large_matroid_operations():
    matroid = UniformMatroid(frozenset(range(100)), 50)
    matroid.contract(50)
    assert 50 not in matroid.groundset
    assert matroid.k == 49
    matroid.delete(51)
    assert 51 not in matroid.groundset
    assert matroid.k == 49 