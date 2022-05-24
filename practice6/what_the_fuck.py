def f(g, x):
    def func(size):
        return ' '.join([g(x) for i in range(size)])

    return func


def f1(x):
    return '*' * x


f2 = f(f1, 2)
print(f2(10))
