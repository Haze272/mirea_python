import math


def main(x):
    result = 0
    if x < 13:
        result = pow(x, 5)
    elif x >= 13 and x < 87:
        result = pow(x, 7) - 1 - (pow(math.ceil(x), 3) / 54)
    elif x >= 87:
        result = pow(math.floor(x), 3)

    return result

print(main(162))  # 4.25e+06
print(main(112))  # 1.40e+06