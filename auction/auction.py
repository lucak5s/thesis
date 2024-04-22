from auction.bidder import Bidder
from typing import List

def unit_step_auction (matroid, bidders: List[Bidder]):
  base = frozenset()
  price = 0
  while not matroid.is_empty():
    critical_elements = get_critical_elements(bidders, price)
    for critical_element in critical_elements:
      print(f'delete element {critical_element}')
      matroid.delete(critical_element)
      for bidder in bidders:
        bidder.drop_interest(critical_element)
        cocircuit = matroid.cocircuit(bidder.get_all_elements())
        if not cocircuit: continue
        chosen_element = bidder.choose_element_to_buy(cocircuit)
        print(f'award element {chosen_element} to bidder {bidder.name} at price ${price}')
        bidder.award_element(chosen_element)
        base = base.union(frozenset([chosen_element]))
        print(f'contract element {chosen_element}')
        matroid.contract(chosen_element)
    price += 1
  return base
    
def get_critical_elements(bidders: List[Bidder], price: int):
  critical_elements = frozenset()
  for bidder in bidders:
    critical_elements = critical_elements.union(bidder.get_critical_elements(price))
  return critical_elements