import numpy as np

b = np.array([[11, 12, 13],
              [21, 22, 23],
              [31, 32, 33]])

print(b)
print(b[1][1])

for i in range(3):
    for j in range(3):
        print(b[i][j])