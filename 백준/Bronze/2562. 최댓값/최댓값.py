prev = 0
for i in range(1, 10):
    cur = int(input())
    if cur > prev:
        prev = cur
        idx = i
print(prev)
print(idx)