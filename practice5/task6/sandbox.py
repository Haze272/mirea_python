# Реализация факториала с ошибкой
def wrong_fact(n):
    assert n >= 0, f'ошибочный аргумент {n}'
    return n * wrong_fact(n - 1)


if __name__ == "__main__":
    wrong_fact(1)  # AssertionError
