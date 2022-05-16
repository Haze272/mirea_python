import math


def main(x, z):
    sum = 0
    n = 3

    for i in range(3):
        sum += math.cos(68*(z[i//4])**2 - (x[2-i//2]) - 79*(x[2-i])**3)**3

    return 28 * sum


arr = [0.95, 0.06, 0.24]
arr1 = [-0.12, -0.09, 0.37]
print(main(arr, arr1))

arr = [-0.1, -0.16, 0.77]
arr1 = [-0.59, -0.7, 0.17]
print(main(arr, arr1))
