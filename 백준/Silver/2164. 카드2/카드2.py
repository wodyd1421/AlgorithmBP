from collections import deque
n = int(input())
deq = deque(range(1, n+1))
for _ in range(n-1):
    deq.popleft()
    deq.rotate(-1)
print(deq[0])