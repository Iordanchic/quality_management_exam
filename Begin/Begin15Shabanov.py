import random
import math

print("Пи:", math.pi)

S = random.randrange(1,100)
R = math.sqrt(S / math.pi)
L = 2 * math.pi * R

print("Радиус окружности: ", R)
print("Площадь круга: ", S)
print("Длина окружности: ", L)
									
