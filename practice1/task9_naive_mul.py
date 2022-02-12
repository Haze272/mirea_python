def naive_mul(x, y):
    r = x;
    for i in range(0, y - 1):
        x = x + r;
    return x

if __name__ == '__main__':
    for i in range(100):
        for j in range(100):
            print(i + 1, " * ", j + 1, " = ", naive_mul(i + 1, j + 1))