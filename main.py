from runtime_comparison.planar_graphic_linear import planar_graphic_linear_comparison
from runtime_comparison.uniform_partition_gammoid_linear import uniform_partition_gammoid_linear_comparison
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

def plot_planar_graphic_linear_comparision(groundset_sizes, density_type, plot_title):
  runtimes = planar_graphic_linear_comparison(groundset_sizes, density_type=density_type)
    
  plt.figure(figsize=(5, 8))
  plt.plot(groundset_sizes, runtimes['planar_runtimes'], label='Planar Matroid', color='black', linewidth=2)
  plt.plot(groundset_sizes, runtimes['graphic_runtimes'], label='Graphic Matroid', color='green', linewidth=2)
  plt.plot(groundset_sizes, runtimes['linear_runtimes'], label='Linear Matroid', color='blue', linewidth=2)
  
  plt.xlabel('Size of Ground Set')
  plt.ylabel('Runtime (s)')
  plt.title(plot_title, fontstyle='italic')
  plt.legend(loc='upper left')
  plt.xlim(min(groundset_sizes), max(groundset_sizes)) 
  plt.ylim(0, 60)
  plt.show()

def plot_uniform_partition_gammoid_linear_comparison(groundset_sizes, k_ratio, plot_title, linear_matroid_limit=None):
  if not linear_matroid_limit: linear_matroid_limit = groundset_sizes[-1]
  runtimes = uniform_partition_gammoid_linear_comparison(groundset_sizes, k_ratio, linear_matroid_limit)

  plt.figure(figsize=(5, 8))
  plt.plot(groundset_sizes, runtimes['uniform_runtimes'], label='Uniform Matroid', color='red', linewidth=6)
  plt.plot(groundset_sizes, runtimes['partition_runtimes'], label='Partition Matroid', linestyle=':', color='black', linewidth=6)
  plt.plot(groundset_sizes, runtimes['gammoid_runtimes'], label='Gammoid', color='green', linewidth=2)
  plt.plot(groundset_sizes[:groundset_sizes.index(linear_matroid_limit) + 1], runtimes['linear_runtimes'], label='Linear Matroid', color='blue', linewidth=2)

  plt.xlabel('Size of Ground Set')
  plt.ylabel('Runtime (s)')
  plt.title(plot_title, fontstyle='italic')
  plt.legend(loc='upper left')
  plt.xlim(min(groundset_sizes), max(groundset_sizes)) 
  plt.ylim(0, 35)
  plt.show()

### Planar - Graphic - Linear ###

plot_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250], 'sparse', r'$|V| = |E|$')
plot_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250], 'semi-dense', r'$|V| = |E| / 2$')
plot_planar_graphic_linear_comparision([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250], 'dense', r'$|V| = |E| / 3 + 6$')

### Uniform - Partition - Gammoid - Linear ###

plot_uniform_partition_gammoid_linear_comparison([10, 20, 30, 40, 50, 60, 70, 80, 90], 'low-k', r'$k = 0.1n$')
plot_uniform_partition_gammoid_linear_comparison([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 36, 40, 42, 50, 60, 70, 80, 90], 'mid-k',  r'$k = 0.5n$', 42)
plot_uniform_partition_gammoid_linear_comparison([10, 12, 14, 16, 18, 20, 22, 24, 26, 30, 36, 40, 42, 50, 60, 70, 80, 90], 'high-k', r'$k = 0.9n$', 26)