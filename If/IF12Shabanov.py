import random

A = random.randrange(-30,30)
B = random.randrange(-30,30)
C = random.randrange(-30,30)

print("Число A:", A)
print("Число B:", B)
print("Число C:", C)

if A < B:
    mn = A
else:
    mn = B
if mn > C:
    mn = C
    
print()    
print("Минимум:", mn)
