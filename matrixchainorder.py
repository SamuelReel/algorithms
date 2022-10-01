import numpy as np
import math


def matrixchainorder(p):
    n = len(p) - 1
    m = np.empty(shape=(n + 1, n + 1), dtype='object')
    s = np.empty(shape=(n + 1, n + 1), dtype='object')

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = math.inf
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print(m)
    print(s)
    printoptimalparens(s, 1, n)


def printoptimalparens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        printoptimalparens(s, i, s[i][j])
        printoptimalparens(s, s[i][j] + 1, j)
        print(")", end="")


P = [3, 4, 5, 6]

matrixchainorder(P)
