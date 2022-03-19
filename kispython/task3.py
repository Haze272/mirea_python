import math


def main(b, n, a, z):
    sum1 = 0
    for j in range(1, b + 1):
        sum1 += (1 + 60 * j)**6 / 39

    sum2 = 0
    for j1 in range(1, a + 1):
        for i in range(1, n + 1):
            for k in range(1, b + 1):
                num1 = math.exp(i**2 - j1**3 - (z/52))**3
                num2 = (94 * math.sqrt(k))
                sum2 += (num1 - num2)

    return sum1 - sum2


print(main(4, 5, 7, -0.26))
print(main(4, 7, 7, -0.41))