import sympy as sp

class LinearMatroid:
  def __init__(self, matrix: sp.Matrix):
    self.dual_matrix = self.derive_dual_representation(matrix)
    self.deleted_columns = frozenset()
  
  def is_empty(self):
    return len(self.deleted_columns) == self.dual_matrix.shape[1]
  
  def derive_dual_representation(self, matrix):
    rref_matrix, identity_matrix_columns = matrix.rref()

    not_identity_matrix_columns = [index for index in range(rref_matrix.cols) if index not in identity_matrix_columns]
    
    nonzero_rows = [i for i in range(rref_matrix.rows) if any(rref_matrix[i, j] != 0 for j in range(rref_matrix.cols))]

    rref_matrix = rref_matrix[nonzero_rows, :]
  
    dual_matrix = rref_matrix[:, not_identity_matrix_columns]
    dual_matrix = dual_matrix.transpose()
    dual_matrix = dual_matrix * (-1)
  
    I = sp.eye(dual_matrix.rows)
    dual_matrix = dual_matrix.row_join(I)

    order = list(identity_matrix_columns) + not_identity_matrix_columns
    dual_matrix = dual_matrix[:, [order.index(i) for i in range(len(order))]]
    return dual_matrix

  def cocircuit(self, X: frozenset) -> frozenset:
    X = X.difference(self.deleted_columns)
    
    indices = [index for index in X]
    matrix = self.dual_matrix[:, indices]
    rref_matrix = matrix.rref()
    
    if len(rref_matrix[1]) == matrix.cols: return frozenset()
    i = len(rref_matrix[1])
    for index in range(1, len(rref_matrix[1])):
      if rref_matrix[1][index] != rref_matrix[1][index-1] + 1:
        i = index
        break
    
    cocircuit = frozenset({indices[i]})
    dependent_column = rref_matrix[0][:, i]
    for i in range(len(dependent_column)):
      if dependent_column[i] != 0:
        cocircuit = cocircuit.union(frozenset([indices[i]]))
 
    return cocircuit

  def delete(self, element):
    if element in self.deleted_columns: return
    self.deleted_columns = self.deleted_columns.union(frozenset({element}))

    rows = self.dual_matrix.rows
    
    pivot_row = None
    for i in range(rows):
      if self.dual_matrix[i, element] != 0:
        pivot_row = i
        break
    
    if pivot_row is None: return
  
    self.dual_matrix[pivot_row, :] = self.dual_matrix[pivot_row, :] / self.dual_matrix[pivot_row, element]
    
    for i in range(rows):
      if i != pivot_row:
        self.dual_matrix[i, :] = self.dual_matrix[i, :] - self.dual_matrix[i, element] * self.dual_matrix[pivot_row, :]
    
    self.dual_matrix.row_del(pivot_row)
 
  def contract(self, element):
    self.deleted_columns = self.deleted_columns.union(frozenset({element}))
  