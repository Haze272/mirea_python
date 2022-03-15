import math


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def main(z):
    step1 = pow(z + 1, 2)
    step2 = 96 * (pow(z, 2) / 29 - 94 * pow(z, 3))
    result = step1 - step2

    step3 = pow(z, 3)
    if step3 < 0:
        step3 = -math.ceil(-step3)
    step4 = pow(step3, 5)
    result /= step4

    step5 = pow(pow(z, 2) - 1, 4)
    step6 = 36 - 77 * pow(29 * pow(z, 3), 4)
    step7 = step5 / step6
    result += step7

    return result

print(main(-0.95))
print(main(-0.75))