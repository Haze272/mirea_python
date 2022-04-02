import math


def main(z):
    sum = 0

    for i in range(len(z)):
        difficult1 = pow(z[math.trunc(i/3)], 3)
        difficult2 = pow(z[math.trunc(i/3)], 2)
        substraction_result = difficult1 - 8 * difficult2
        sum += 66 * pow(substraction_result, 2)

    return sum


arr = [0.35, -0.93, 0.94, 0.59, 0.05, 0.75, -0.52]
print(main(arr))
arr = [0.24, -0.48, 0.17, -0.5, 0.52, -0.62, -0.26]
print(main(arr))
