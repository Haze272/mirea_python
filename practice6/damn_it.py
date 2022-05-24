def twice(f):
    def g(x):
        return f(f(x))

    return g


print((lambda x: x * x)(2))
print(twice(lambda x: x * x)(2))
print(twice(twice(lambda x: x * x))(2))
print(twice(twice(twice(lambda x: x * x)))(2))
