from matroids.matroid import Matroid

class SchedulingMatroid(Matroid):
  def __init__(self, job_with_deadlines: dict):
    self.deadlines = job_with_deadlines
    self.dual_deadlines = dual_deadlines(job_with_deadlines)
    
  def full_rank(self) -> int:
    sorted_jobs = sorted(self.deadlines, key=self.deadlines.get)
    scheduled_jobs = 0
    for job in sorted_jobs:
        job_start = self.deadlines[job] - 1
        if job_start >= scheduled_jobs:
            scheduled_jobs += 1
    return scheduled_jobs

  def unique_cocircuit(self, X: frozenset) -> frozenset:
    sorted_jobs = sorted(X, key= lambda job: self.dual_deadlines[job])
    cocircuit = frozenset()
    scheduled_jobs = 0
    for job in sorted_jobs:
      job_start = self.dual_deadlines[job] - 1
      cocircuit = cocircuit.union(frozenset({job}))
      if job_start < scheduled_jobs: return cocircuit
      scheduled_jobs += 1
    return frozenset()
  
  def contract(self, element):
    for job, deadline in self.deadlines.items():
      if deadline >= self.deadlines[element]:
        self.deadlines[job] -= 1
    self.deadlines.pop(element)
    self.dual_deadlines.pop(element)

  def delete(self, element):
    for job, deadline in self.dual_deadlines.items():
      if deadline >= self.dual_deadlines[element]:
        self.dual_deadlines[job] -= 1
    self.deadlines.pop(element)
    self.dual_deadlines.pop(element)


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








