import numpy as np


def CreateMatrix():
    n = int(input("So hang ma tran vuong (n<10)"))
    while 10 < n:
        n = int(input("Nhap lai So hang ma tran vuong (n<10)"))
    n = int(n)
    a = np.zeros(n, n)
    return a
