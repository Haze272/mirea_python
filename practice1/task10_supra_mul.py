def fast_mul(a, b):
    result = 0
    while a > 1:
        a //= 2
        b *= 2
        if a % 2 != 0:
            result += b
    return result

def fast_pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a

    result = 0
    b1 = a
    for i in range(b - 1):
        result1 = result
        while a > 1:
            a //= 2
            b1 *= 2
            if a % 2 != 0:
                result1 += b1
        result += result1

    return result

print(fast_mul(10, 15))
print(fast_pow(2, 8))