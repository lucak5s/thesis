from matroids.matroid import Matroid
from auctions.bidder import Bidder
from typing import List

def unit_step_auction (matroid: Matroid, bidders: List[Bidder]):
  base = frozenset()
  price = 0
  full_rank = matroid.rank(matroid.groundset)

  while len(base) < full_rank and price < 10:
    price += 1
    critical_elements = get_critical_elements(bidders, price)
    for critical_element in critical_elements:
      matroid.delete(critical_element)
      for bidder in bidders:
        cocircuit = matroid.unique_cocircuit(bidder.get_all_elements())
        if not cocircuit: continue
        chosen_element = bidder.choose_element_to_buy(cocircuit)
        print(f'award element {chosen_element} to bidder {bidder.name} at price ${price}')
        base = base.union(frozenset([chosen_element]))
        matroid.contract(chosen_element)
        
  
  return base

def get_critical_elements(bidders: List[Bidder], price: int):
  critical_elements = frozenset()
  for bidder in bidders:
    critical_elements = critical_elements.union(bidder.get_critical_elements(price))
  return critical_elements