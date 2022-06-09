import random

A = random.randrange(-10,10)
B = random.randrange(-10,10)
C = random.randrange(-10,10)

print("A = ", A)
print("B = ", B)
print("C = ", C)

a = (A>0)
b = (B>0)
c = (C>0)
x = (a and b and c)

print("A положительно: ", a)
print("B положительно: ", b)
print("C положительно: ", c)
print("Каждое из чисел A, B, C положительное: ", x)
							
