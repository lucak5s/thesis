from runtime_comparison.planar_graphic_linear import planar_graphic_linear_comparison
import matplotlib.pyplot as plt

### Planar - Graphic - Linear ###

amounts_of_nodes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
density_types = ['sparse', 'semi-dense', 'dense']

for density in density_types:
    runtimes = planar_graphic_linear_comparison(amounts_of_nodes, density_type=density)
    
    plt.plot(amounts_of_nodes, runtimes['planar_runtimes'], label='Planar Matroid')
    plt.plot(amounts_of_nodes, runtimes['graphic_runtimes'], label='Graphic Matroid')
    plt.plot(amounts_of_nodes, runtimes['linear_runtimes'], label='Linear Matroid')
    
    plt.title(f'{density.capitalize()} Graph')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.show()

### Uniform - Partition - Gammoid - Linear ###