import math


def main(z):
    sum = 0
    for i in range(1, len(z) + 1):
        num1 = pow(z[math.ceil(i/3)], 3)
        num2 = 8 * pow(z[math.ceil(i/3)], 2)
        sum += (num1 - num2)**2

    return sum * 66

arr = [0.35, -0.93, 0.94, 0.59, 0.05, 0.75, -0.52]
print(main(arr))
arr = [0.24, -0.48, 0.17, -0.5, 0.52, -0.62, -0.26]
print(main(arr))