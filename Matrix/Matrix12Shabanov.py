import random
import numpy

M = random.randrange(2,10)
N = random.randrange(2,10)
print("M = ",M,"; N = ",N)
a = numpy.zeros((M, N))
k = 0
for i in range(M):
    for j in range(N):
        k += 1
        a[i][j] = k
print(a)
for i in range(M):
    for j in range(N):
        if j%2 == 0:
            print(a[i][j],end=" ")
        else:
            print(a[M-1-i][j],end=" ")
    print()
