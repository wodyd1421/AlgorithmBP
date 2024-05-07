a, b = map(int, input().split())
c = a * b
a, b = max(a, b), min(a, b)
while b != 0:
    a %= b
    a, b = b, a
print(a)
print(c//a)