import math


def main(z):
    if pow(z, 3) < 0:
        zerodiv = math.ceil(-(pow(z, 3)))
    else:
        zerodiv = math.ceil(pow(z, 3))
    num1 = (((z + 1) * (z + 1)) - 96 * ((z * z / 29) - (94 * z * z * z)))
    denum1 = pow(zerodiv, 5)
    num2 = pow((z * z - 1), 4)
    denum2 = (36 - (77 * pow((29 * z * z * z), 4)))
    result = round((num1/denum1 + num2/denum2), 2)

    return abs(result)

print(main(-0.95))