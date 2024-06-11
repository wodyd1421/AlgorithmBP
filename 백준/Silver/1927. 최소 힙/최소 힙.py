import sys
input = sys.stdin.readline

import heapq

heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)