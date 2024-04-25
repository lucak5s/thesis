import sympy as sp

def uniform_matrix_representation(n, k):
  matrix = []
  for i in range(1, k + 1):
    row = [j**(i-1) for j in range(1, n + 1)]
    matrix.append(row)
  return sp.Matrix(matrix)