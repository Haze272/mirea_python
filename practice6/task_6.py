def make_perf(counter):
    def dec(func):
        func_name = func.__name__

        def holder(*args):
            counter[func_name] = counter.get(func_name, 0) + 1
            res = func(*args)
            return res

        return holder

    return dec


def memoization(func):
    cache = {}

    def wrapper(*args):
        value = args[0]
        if not cache.get(value):
            cache[value] = func(value)
        return cache.get(value)

    return wrapper


PERF = {}
perf = make_perf(PERF)


@perf
def fact_without_memo(n):
    if n == 1:
        return 1
    return n * fact_without_memo(n - 1)


@memoization
@perf
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


@perf
def fib_without_memo(n):
    if n <= 1:
        return n
    else:
        return fib_without_memo(n - 1) + fib_without_memo(n - 2)


@memoization
@perf
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fact_without_memo(10))
    print(fact(10))
    print(fib_without_memo(27))
    print(fib(27))

    print("\nCounter of function calls:")
    for i in PERF:
        print(i, ": ", PERF[i])
