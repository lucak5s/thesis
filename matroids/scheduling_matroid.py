from matroids.matroid import Matroid

class SchedulingMatroid(Matroid):
  def __init__(self, job_with_deadlines: dict, job_length: int):
    self.deadlines = job_with_deadlines
    self.dual_deadlines = get_dual_deadlines(job_with_deadlines)
    self.job_length = job_length
    
  def full_rank(self) -> int:
    sorted_jobs = sorted(self.deadlines, key= lambda job: self.deadlines[job])
    rank = 0
    current_time = 0
    for job in sorted_jobs:
      job_start = self.deadlines[job] - self.job_length
      if job_start >= current_time:
        rank += 1
        current_time = job_start + self.job_length
    return rank

  def unique_cocircuit(self, X: frozenset) -> frozenset:
    sorted_jobs = sorted(X, key= lambda job: self.dual_deadlines[job])
    cocircuit = frozenset()
    current_time = 0
    for job in sorted_jobs:
      job_start = self.dual_deadlines[job] - self.job_length
      cocircuit = cocircuit.union(frozenset({job}))
      if job_start < current_time: return cocircuit
      current_time = job_start + self.job_length
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