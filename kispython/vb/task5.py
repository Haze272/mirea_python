import math


def main(x, z):
    sum = 0
    n = len(z)-1

    for i in range(1, n):
        difficult1 = 68 * pow(z[math.trunc(i/4)], 2)
        difficult2 = x[n + 1 - math.trunc(i/2)]
        difficult3 = 79 * pow(x[n + 1 - i], 3)

        substraction_result = math.cos(difficult1 - difficult2 - difficult3)
        sum += 28 * pow(substraction_result, 3)

    return sum


arr = [0.95, 0.06, 0.24]
arr1 = [-0.12, -0.09, 0.37]
print(main(arr, arr1))

arr = [-0.1, -0.16, 0.77]
arr1 = [-0.59, -0.7, 0.17]
print(main(arr, arr1))