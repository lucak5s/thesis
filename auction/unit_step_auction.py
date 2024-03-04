from matroids.matroid import Matroid
from auction.bidder import Bidder
from typing import List

def unit_step_auction (matroid: Matroid, bidders: List[Bidder]):
  base = frozenset()
  price = 0
  full_rank = matroid.full_rank()

  while True:
    price += 1
    critical_elements = get_critical_elements(bidders, price)
    for critical_element in critical_elements:
      print(f'delete element {critical_element}')
      matroid.delete(critical_element)
      j = 0
      while j < len(bidders):
        bidder = bidders[j]
        j += 1
        cocircuit = matroid.unique_cocircuit(bidder.get_all_elements())
        if not cocircuit: continue
        print(cocircuit)
        chosen_element = bidder.choose_element_to_buy(cocircuit)
        bidder.award_element(chosen_element, price)
        base = base.union(frozenset([chosen_element]))
        matroid.contract(chosen_element)
        j = 0
        if len(base) == full_rank: return base

def get_critical_elements(bidders: List[Bidder], price: int):
  critical_elements = frozenset()
  for bidder in bidders:
    critical_elements = critical_elements.union(bidder.get_critical_elements(price))
  return critical_elements