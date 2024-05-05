from runtime_comparison.planar_graphic_linear import planar_graphic_linear_comparison
from runtime_comparison.uniform_partition_gammoid_linear import uniform_partition_gammoid_linear_comparison
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

### Planar - Graphic - Linear ###

amounts_of_nodes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
density_types = ['sparse', 'semi-dense', 'dense']
density_title_map = {
  'sparse': r'$|E| = |V|$',
  'semi-dense': r'$|E| = 2|V|$',
  'dense': r'$|E| = 3|V| - 6$'
}

for density in density_types:
    runtimes = planar_graphic_linear_comparison(amounts_of_nodes, density_type=density)
    
    plt.figure(figsize=(5, 8))
    plt.plot(amounts_of_nodes, runtimes['planar_runtimes'], label='Planar Matroid', color='black', linewidth=2)
    plt.plot(amounts_of_nodes, runtimes['graphic_runtimes'], label='Graphic Matroid', color='green', linewidth=2)
    plt.plot(amounts_of_nodes, runtimes['linear_runtimes'], label='Linear Matroid', color='blue', linewidth=2)
    
    plt.xlabel('Number of Nodes')
    plt.ylabel('Runtime (s)')
    plt.title(density_title_map[density], fontstyle='italic')
    plt.legend()
    plt.xlim(min(amounts_of_nodes), max(amounts_of_nodes)) 
    plt.show()

### Uniform - Partition - Gammoid - Linear ###

groundset_sizes = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 36, 40, 42, 50, 60, 70, 80, 90]
k_ratios = ['low-k', 'mid-k', 'high-k']
k_ratio_title_map = {
  'low-k': r'$k = 0.1n$',
  'mid-k': r'$k = 0.5n$',
  'high-k': r'$k = 0.9n$'
}
k_ratio_linear_matroid_limit_map = {
  'low-k': 90,
  'mid-k': 42,
  'high-k': 26
}

for ratio in k_ratios:
  runtimes = uniform_partition_gammoid_linear_comparison(groundset_sizes, ratio, k_ratio_linear_matroid_limit_map[ratio])

  plt.figure(figsize=(5, 8))
  plt.plot(groundset_sizes, runtimes['uniform_runtimes'], label='Uniform Matroid', color='red', linewidth=3)
  plt.plot(groundset_sizes, runtimes['partition_runtimes'], label='Partition Matroid', linestyle='--', color='black', linewidth=2)
  plt.plot(groundset_sizes, runtimes['gammoid_runtimes'], label='Gammoid', color='green', linewidth=2)
  plt.plot(groundset_sizes[:groundset_sizes.index(k_ratio_linear_matroid_limit_map[ratio]) + 1], runtimes['linear_runtimes'], label='Linear Matroid', color='blue', linewidth=2)

  plt.xlabel('Size of Ground Set')
  plt.ylabel('Runtime (s)')

  plt.title(k_ratio_title_map[ratio], fontstyle='italic')
  plt.legend(loc='upper left')
  plt.xlim(min(groundset_sizes), max(groundset_sizes)) 
  plt.ylim(-1, max(runtimes['gammoid_runtimes']))
  plt.show()
