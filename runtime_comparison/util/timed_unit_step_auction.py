import time
from auction.auction import unit_step_auction

def timed_unit_step_auction(matroid, bidders):
    start_time = time.time()
    base = unit_step_auction(matroid, bidders)
    end_time = time.time()
    return (base, end_time - start_time)