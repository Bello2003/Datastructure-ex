def to_sparse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    sparse = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append((i, j, matrix[i][j]))
    return sparse

# Exemple
mat = [[0, 0, 3],
       [4, 0, 0],
       [0, 5, 0]]
print(to_sparse(mat))
