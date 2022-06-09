import random

N = random.randrange(1,10)
print('N = ', N)
P = 1.0

for i in range(1,N+1):
    x = 1 + i*0.1
    P *= x
    print(i," : ",x," : ",P)
print("Произведение = ",P)
