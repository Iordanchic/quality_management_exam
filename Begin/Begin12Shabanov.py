import random
import math

a = random.randrange(1,100)
b = random.randrange(1,100)

#a = 3
#b = 4

print("Катет 1: ", a)
print("Катет 2: ", b)

c = math.sqrt(a**2 + b**2)
P = a + b + c

print("Гипотенуза: ", c)
print("Периметр: ", P)
									
