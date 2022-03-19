def main(n):
    if n == 0:
        return -0.39
    elif n >= 1:
        return (1 - pow(abs(main(n - 1)), 2) - main(n - 1))


print(main(1))
print(main(8))