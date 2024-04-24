import runtime_comparison.planar_graphic_linear
import matplotlib.pyplot as plt

amount_of_nodes = []

### Sparse Graph ###
sparse_runtimes = planar_graphic_linear_comparison(amount_of_nodes, ratio='sparse')

plt.plot(amount_of_nodes, sparse_runtimes.planar_runtimes, marker='x') 
plt.plot(amount_of_nodes, sparse_runtimes.graphic_runtimes, marker='y') 
plt.plot(amount_of_nodes, sparse_runtimes.linear_runtimes, marker='z') 

plt.title('Sparse Graph / node-edge ratio: 1')
plt.xlabel('Number of Nodes')
plt.ylabel('Runtime (ms)')
plt.show()

### Semi-Dense Graph ###
semi_dense_runtimes = planar_graphic_linear_comparison(amount_of_nodes, ratio='semi-dense')

plt.plot(amount_of_nodes, sparse_runtimes.planar_runtimes, marker='x') 
plt.plot(amount_of_nodes, sparse_runtimes.graphic_runtimes, marker='y') 
plt.plot(amount_of_nodes, sparse_runtimes.linear_runtimes, marker='z') 

plt.title('Sparse Graph / node-edge ratio: 1')
plt.xlabel('Number of Nodes')
plt.ylabel('Runtime (ms)')
plt.show()

### Dense Graph ###
dense_runtimes = planar_graphic_linear_comparison(amount_of_nodes, ratio='dense')

plt.plot(amount_of_nodes, sparse_runtimes.planar_runtimes, marker='x') 
plt.plot(amount_of_nodes, sparse_runtimes.graphic_runtimes, marker='y') 
plt.plot(amount_of_nodes, sparse_runtimes.linear_runtimes, marker='z') 

plt.title('Sparse Graph / node-edge ratio: 1')
plt.xlabel('Number of Nodes')
plt.ylabel('Runtime (ms)')
plt.show()