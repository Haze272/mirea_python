
def main(x):
    result = 0

    A = x & 0b11111111
    B = (x >> 8) & 0b11111
    C = (x >> 13) & 0b1111111111111111
    D = (x >> 29) & 0b1
    E = (x >> 30) & 0b11

    result |= A << 24
    result |= C << 8
    result |= B << 3
    result |= E << 1
    result |= D << 0

    return result


print(main(0x74bf87c8))  # 0xc8a5fc3b
print(main(0x646fae0d))  # 0x0d237d73
