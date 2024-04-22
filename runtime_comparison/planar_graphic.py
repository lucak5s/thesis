from matroid.graphic_matroid import GraphicMatroid
from matroid.planar_matroid import PlanarMatroid
from auction.bidder import Bidder
from auction.auction import unit_step_auction
import copy

def add_edge_if_planar(G, u, v):
    G.add_edge(u, v)
    planar, _ = nx.check_planarity(G)
    if not planar:
        G.remove_edge(u, v)
        return False
    return True

def random_planar_graph(num_nodes, attempts=1000):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for _ in range(attempts):
        u, v = random.sample(G.nodes, 2)
        add_edge_if_planar(G, u, v)
    return G

num_nodes = 50
num_attempts = 300
G = random_planar_graph(num_nodes, num_attempts)

vertices = frozenset(G.nodes())
edges = frozenset([frozenset(edge) for edge in G.edges()])

bidders_graphic = [Bidder({edge: random.randint(1, 100)}, str(edge)) for edge in edges]
bidders_planar = copy.deepcopy(bidders_graphic)

graphic_matroid = GraphicMatroid(vertices, edges)
graphic_base = unit_step_auction(graphic_matroid, bidders_graphic)
print('base:', graphic_base)

###

planar_matroid = PlanarMatroid(edges)
planar_base = unit_step_auction(planar_matroid, bidders_planar)
print('base:', planar_base)