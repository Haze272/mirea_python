def fast_mul_gen(a, b):
    result = 0
    print("Result =", result)
    while a:
        if a % 2 != 0:
            print("Result +=", b)
            result += b
        print(b, "+=", b)
        a //= 2
        b *= 2
    print("Result =", result)

x = int(input())
y = int(input())
print("x =", x, "y =", y)
fast_mul_gen(x, y)