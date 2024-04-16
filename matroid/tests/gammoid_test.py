import pytest
from matroid.gammoid import FlowNetwork


### Flow Network ###

def test_initialization():
    vertices = ['a', 'b', 'c']
    edges = [('a', 'b'), ('b', 'c')]
    starting_vertices = ['a']
    destination_vertices = ['c']
    fn = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)

    assert 's' in fn.graph
    assert 't' in fn.graph
    assert 'a_in' in fn.graph and 'a_out' in fn.graph
    assert 'b_in' in fn.graph and 'b_out' in fn.graph
    assert 'c_in' in fn.graph and 'c_out' in fn.graph

    assert fn.graph['s']['a_in'] == 1
    assert fn.graph['a_out']['b_in'] == 1
    assert fn.graph['b_out']['c_in'] == 1
    assert fn.graph['c_out']['t'] == 1

def test_find_augmenting_path():
    vertices = ['a', 'b', 'c']
    edges = [('a', 'b'), ('b', 'c')]
    starting_vertices = ['a']
    destination_vertices = ['c']
    fn = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)

    path = fn.find_augmenting_path()
    assert 't' in path  

    path_with_element = fn.find_augmenting_path(element='a')
    print(path_with_element)
    assert 'a_in' in path_with_element  
    assert 't' in path 

def test_augment_flow():
    vertices = ['a', 'b', 'c']
    edges = [('a', 'b'), ('b', 'c')]
    starting_vertices = ['a']
    destination_vertices = ['c']
    fn = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)
    
    path = fn.find_augmenting_path()
    fn.augment_flow(path)
    
    assert fn.graph['s']['a_in'] == 0
    assert fn.graph['a_out']['b_in'] == 0
    assert fn.graph['b_out']['c_in'] == 0
    assert fn.graph['c_out']['t'] == 0

    assert fn.graph['a_in']['s'] == 1
    assert fn.graph['b_in']['a_out'] == 1
    assert fn.graph['c_in']['b_out'] == 1
    assert fn.graph['t']['c_out'] == 1


### Base & Full Rank ###


### Dual Matroid ###


### Cocircuit ###


### Delete ###


### Contract ###


