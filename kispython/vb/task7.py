def main(x):
    result = 0

    A = x & 0b1111111111
    B = (x >> 10) & 0b111111
    C = (x >> 16) & 0b1111
    D = (x >> 20) & 0b11111111111111

    result |= C << 28
    result |= B << 22
    result |= A << 12
    result |= D << 0

    return result


print(main(0x70be177e))  # 0xe177e70b
print(main(0xef8ac481))  # 0xac481ef8