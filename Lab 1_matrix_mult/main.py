import numpy as np
import random
import time


def mult_and_add_T(c_i, a_ip, b_p):
    n = b_p.size
    for j in range(n):
        c_i[j] += a_ip * b_p[j]


def matix_multiply(A, B):
    m = A.shape[0]
    k = B.shape[0]
    n = B.shape[1]

    C = np.zeros((m, n))
    for p in range(k):
        for i in range(m):
            mult_and_add_T(C[i], A[i,p], B[p])

    return C


A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

D = np.array([[random.random()]*100]*100)
E = np.array([[random.random()]*100]*100)

start_time = int(round(time.time() * 1000))
# C = matix_multiply(D, E)
C = D @ E
stop_time = int(round(time.time() * 1000))

print(stop_time - start_time)
