from matroids.matroid import Matroid

class SchedulingMatroid(Matroid):
  def __init__(self, job_with_deadlines: dict):
    self.deadlines = job_with_deadlines
    self.dual_deadlines = get_dual_deadlines(job_with_deadlines)
    
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


def get_dual_deadlines(deadlines: dict) -> dict:
  sorted_jobs = sorted(deadlines, key= lambda job: deadlines[job], reverse=True)

  curr_deadline = deadlines[sorted_jobs[0]]
  jobs_with_curr_deadline = set(sorted_jobs[0])
  offset = 0
  dual_deadlines = {}

  for job in sorted_jobs:
    if deadlines[job] != curr_deadline:
      offset += len(jobs_with_curr_deadline) - (curr_deadline - deadlines[job])
      for j in jobs_with_curr_deadline:
        dual_deadlines[j] = offset
      jobs_with_curr_deadline.clear()
      curr_deadline = deadlines[job]
    jobs_with_curr_deadline.add(job)

  if jobs_with_curr_deadline:
    offset += len(jobs_with_curr_deadline) - (curr_deadline)
    for j in jobs_with_curr_deadline:
      dual_deadlines[j] = offset
  
  return dual_deadlines