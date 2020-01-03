# Creando una funcion que revisa las matrices

import numpy as np

B = np.matrix([[1, 2], [3, 4]])


def mult(A):
    M = np.matrix(np.zeros((2, 2)))
    for i in range(0, M.shape[0]):
        for j in range(0, M.shape[1]):
            M[i, j] = A[i, j]*2
    return(M)


renglones = B.shape[0]
columnas = B.shape[1]

print(mult(B))
