import math


def main(n):
    if n == 0:
        return 0.91
    elif n >= 1:
        return math.sin(main(n-1))**3 - 4 - math.exp(9 * main(n-1))


print(main(5))
print(main(2))