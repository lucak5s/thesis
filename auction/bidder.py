class Bidder:
  def __init__(self, valuations, name):
    self.valuations = valuations
    self.name = name

  def get_all_elements(self) -> frozenset:
    elements = frozenset()
    for element in self.valuations:
      elements = elements.union(frozenset([element]))
    return elements
  
  def get_critical_elements(self, price: int) -> frozenset:
    critical_elements = frozenset()
    for element, valuation in self.valuations.items():
      if valuation == price:
        critical_elements = critical_elements.union(frozenset([element]))
      
    return critical_elements
  
  def choose_element_to_buy(self, X: frozenset):
    max_element = None
    max_valuation = float('-inf')
    for element in X:
      if self.valuations[element] > max_valuation:
        max_valuation = self.valuations[element]
        max_element = element
    return max_element
  
  def award_element(self, element):
    self.valuations.pop(element)
    
  def drop_interest(self, element):
    if element in self.valuations: self.valuations.pop(element)