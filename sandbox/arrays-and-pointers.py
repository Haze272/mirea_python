import copy
import math
import random

supra_path = []
path = ['TEXT', 'M', 'ANTLR', 'JULIA', 'MAX']

supra_path.append(path)
print(supra_path)

q = math.factorial(len(path))

for i in range(q):
    govno = copy.copy(path)
    random.shuffle(govno)
    supra_path.append(govno)
print(supra_path)


