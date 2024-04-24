import pytest
from matroid.gammoid import FlowNetwork, Gammoid


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
    vertices = ['a', 'b', 'c', 'd']
    edges = [('a', 'b'), ('b', 'c')]
    starting_vertices = ['a', 'd']
    destination_vertices = ['c', 'd']
    fn = FlowNetwork(vertices, edges, starting_vertices, destination_vertices)

    path = fn.find_augmenting_path()
    assert 't' in path  

    path_with_element = fn.find_augmenting_path(element='a')
    assert 'a_in' in path_with_element  
    assert 't' in path_with_element 
    
    
    path_with_element = fn.find_augmenting_path(element='d')
    assert 't' in path_with_element

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


### Gammoid Init ###
def test_gammoid_initialization():
    vertices = frozenset({'1', '2', '3', '4', '5', '6'})
    edges = frozenset({('1', '2'), ('1', '3'), ('3', '4'), ('2', '4'), ('4', '6'), ('4', '5')})
    starting_vertices = frozenset({'1', '2', '3'})
    destination_vertices = frozenset({'3', '5', '6'})
    
    gammoid = Gammoid(vertices, edges, starting_vertices, destination_vertices)
    
    cocircuit = gammoid.cocircuit(frozenset({'1', '2'}))

    assert cocircuit == frozenset({'1', '2'})
    
### Base ###

### Dual Matroid ###


### Cocircuit ###


### Delete ###


### Contract ###


