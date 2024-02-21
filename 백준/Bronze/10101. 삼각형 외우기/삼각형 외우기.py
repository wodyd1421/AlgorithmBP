a, b, c = int(input().rstrip()), int(input().rstrip()), int(input().rstrip())
if a + b + c != 180:
    print('Error')
elif a != b != c != a:
    print('Scalene')
elif a == b == c:
    print('Equilateral')
else:
    print('Isosceles')