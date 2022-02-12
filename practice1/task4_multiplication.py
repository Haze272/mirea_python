def multi12(num):
    num += num
    num += num
    num += num + num
    return num

def multi16(num):
    num += num
    num += num
    num += num
    num += num
    return num

def multi15(num):
    x = num
    z = num
    x += x
    x += x
    y = x + x
    x = z - y
    x = y - x
    return x

def multi29(num):
    x = num
    num += num
    num += num
    num += num
    num -= x
    num += num
    num += num
    num += x
    return num

print(multi12(3)) # 3 * 12 = 36
print(multi16(3)) # 3 * 16 = 48
print(multi15(3)) # 3 * 15 = 45
print(multi29(3)) # 3 * 29 = 87