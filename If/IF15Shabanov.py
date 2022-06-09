import random

A = random.randrange(-30,30)
B = random.randrange(-30,30)
C = random.randrange(-30,30)

print("Число A:", A)
print("Число B:", B)
print("Число C:", C)

if (C <= A and A <= B) or (C <= B and B <= A):
    m = A + B
elif (B <= A and A <= C) or (B <= C and C <= A):
    m = A + C
elif (A <= C and C <= B) or (A <= B and B <= C):
    m = B + C
    
print()    
print("Сумма:", m)
