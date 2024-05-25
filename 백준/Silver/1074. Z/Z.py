n, r, c = map(int, input().split())
count = 0
while n != 0:
  n -= 1
  if r < 2 ** n and c < 2 ** n:
    count += 2 ** (2 * n) * 0
  if r < 2 ** n and c >= 2 ** n:
    count += 2 ** (2 * n) * 1
    c -= 2 ** n
  if r >= 2 ** n and c < 2 ** n:
    count += 2 ** (2 * n) * 2
    r -= 2 ** n
  if c >= 2 ** n and r >= 2 ** n:
    count += 2 ** (2 * n) * 3
    r -= 2 ** n
    c -= 2 ** n
print(count)