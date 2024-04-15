deadlines_1 = {
  1: set({'g', 'h', 'i'}),
  2: set({'e', 'f'}),
  3: set({'c', 'd'}),
  4: set({'a', 'b'})
}

deadlines_2 = {
  5: set({'g', 'h', 'i'}),
  3: set({'e', 'f'}),
  2: set({'c', 'd'}),
  1: set({'a', 'b'})
}

deadlines_3 = {
  1: set({'a'}),
  3: set({'b', 'c', 'd', 'e'}),
}

deadlines_4 = {
  2: set({'a', 'b', 'c', 'd', 'e'}),
}


def dual_deadlines(deadlines):
  sorted_deadlines = sorted(deadlines)
  dual_deadlines = {}
  previous_dual_deadline = 0

  i = len(sorted_deadlines) - 1
  while i >= 0:
    deadline = sorted_deadlines[i]
    previous_deadline = sorted_deadlines[i-1] if i > 0 else 0
    elements_with_deadline = deadlines[deadline]

    dual_deadline = len(elements_with_deadline) - (deadline - previous_deadline) + previous_dual_deadline
    previous_dual_deadline = dual_deadline
    dual_deadlines[dual_deadline] = dual_deadlines[dual_deadline].union(elements_with_deadline) if dual_deadline in dual_deadlines else elements_with_deadline

    i -= 1

  return dual_deadlines
  
  print(dual_deadlines)


dual_deadlines(deadlines_1)
dual_deadlines(deadlines_2)
dual_deadlines(deadlines_3)
dual_deadlines(deadlines_4)