def uniform_gammoid_representation(groundset, k):
  starting_vertices = groundset
  destination_vertices = frozenset([str(i) + '_dest' for i in range(k)])
  
  edges = []
  for u in starting_vertices:
    for v in destination_vertices:
      edges.append((u, v))
      
  return starting_vertices.union(destination_vertices), edges, starting_vertices, destination_vertices