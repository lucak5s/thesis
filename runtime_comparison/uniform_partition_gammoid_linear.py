from matroid.uniform_matroid import UniformMatroid
from matroid.partition_matroid import PartitionMatroid
from matroid.gammoid import Gammoid
from matroid.linear_matroid import LinearMatroid
from runtime_comparison.util.random_groundset import random_groundset
from runtime_comparison.util.uniform_gammoid_representation import uniform_gammoid_representation
from runtime_comparison.util.uniform_matrix_representation import uniform_matrix_representation
from auction.bidder import Bidder
import random
import time
from auction.auction import unit_step_auction
import threading
import signal
import sys

def timeout_handler(signum, frame):
    raise TimeoutError("Execution exceeded the time limit")

def uniform_partition_gammoid_linear_comparison(groundset_sizes, k_ratio):
  linear_timout = False
  
  linear_runtimes = []
  gammoid_runtimes = []
  partition_runtimes = []
  uniform_runtimes = []
  
  for n in groundset_sizes:
    if k_ratio == 'low-k':
      k = n // 10
    elif k_ratio == 'mid-k':
      k = n // 2
    else:
      k = int((n / 10) * 9)
    
    groundset = random_groundset(n)
    weighted_groundset = [(element, random.randint(1, 1000)) for element in groundset]
    
    # ### Linear Matroid ###
    
    if not linear_timout:
      signal.signal(signal.SIGALRM, timeout_handler)
      signal.alarm(100)
      
      try:
        matrix = uniform_matrix_representation(n, k)
        
        linear_bidders = [Bidder({index: weight}, element) for index, (element, weight) in enumerate(weighted_groundset)]
        index_element_map = {index: element for index, (element, weight) in enumerate(weighted_groundset)}

        start_time = time.time()
        linear_matroid = LinearMatroid(matrix)
        linear_base = unit_step_auction(linear_matroid, linear_bidders)
        end_time = time.time()
        
        linear_base_in_elements = frozenset([index_element_map[index] for index in linear_base])
        
        linear_runtime = end_time - start_time
        linear_runtimes.append(linear_runtime)

      except TimeoutError as e:
          print(e)
          linear_timout = True

      finally:
          signal.alarm(0)

    # ### Gammoid ###
    
    vertices, edges, starting_vertices, destination_vertices = uniform_gammoid_representation(groundset, k)
    gammoid_bidders = [Bidder({element: weight}, element) for element, weight in weighted_groundset]
    
    start_time = time.time()
    gammoid = Gammoid(vertices, edges, starting_vertices, destination_vertices)
    gammoid_base = unit_step_auction(gammoid, gammoid_bidders)
    end_time = time.time()
    
    gammoid_runtime = end_time - start_time
    gammoid_runtimes.append(gammoid_runtime)

    ### Partition Matroid ###
    
    partition_bidders = [Bidder({element: weight}, element) for element, weight in weighted_groundset]
    
    start_time = time.time()
    partition_matroid = PartitionMatroid(groundset, [(groundset, k)])
    partition_base = unit_step_auction(partition_matroid, partition_bidders)
    end_time = time.time()
    
    partition_runtime = end_time - start_time
    partition_runtimes.append(partition_runtime)

    ### Uniform Matroid ###
    
    uniform_bidders = [Bidder({element: weight}, element) for element, weight in weighted_groundset]
    
    start_time = time.time()
    uniform_matroid = UniformMatroid(groundset, k)
    uniform_base = unit_step_auction(uniform_matroid, uniform_bidders)
    end_time = time.time()
    
    uniform_runtime = end_time - start_time
    uniform_runtimes.append(uniform_runtime)
  
  return {
    'linear_runtimes': linear_runtimes,
    'gammoid_runtimes': gammoid_runtimes,
    'partition_runtimes': partition_runtimes,
    'uniform_runtimes': uniform_runtimes
  }
