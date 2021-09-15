def Log2n(n):
    return 1 + Log2n(n / 2) if (n > 1) else 0

n = 32
print(Log2n(n))