import numpy as np

A = np.array([[1, 2, 3],
              [2, 5, 6],
              [4, 8, 9]], dtype=np.float32)


def ldlt_factorization(A):
    n = A.shape[0]
    result = np.zeros([n, n], dtype = np.float32)
    for i in range(n):
        for j in range(i+1):
            if i == j:
                tmp = 0
                for k in range(j):
                    tmp += result[j, k] * result[j, k] * result[k, k]
                result[i, i] = A[i, i] - tmp
            else:
                tmp = 0
                for k in range(j):
                    tmp += result[i, k] * result[j, k] * result[k, k]
                result[i, j] = 1 / (result[j, j] * (A[i, j] - tmp))

    return result


L = ldlt_factorization(A)
print(L)