n = int(input())
state = 1
for i in range(5):
    m = (n-2*i) % 5
    s = (n-2*i) // 5
    if s < 0:
        break
    if not m:
        print(s+i)
        state = 0
if state:
    print(-1)