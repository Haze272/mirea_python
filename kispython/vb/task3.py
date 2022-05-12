import math


def main(n, a, x, m):
    sum1 = 0
    for j in range(1, a + 1):
        for c in range(1, n + 1):
            sum1 += (pow(j, 7) + (c**3 - 9*c*c)**5 + x**6)

    sum2 = 0
    for j in range(1, m + 1):
        for i in range(1, a + 1):
            for k in range(1, n + 1):
                sum2 += (k**6 + 47*pow(i*i+69*j+j**3, 5))

    return sum1 + sum2


print(main(7, 8, -0.66, 2))
print(main(8, 8, -0.06, 2))