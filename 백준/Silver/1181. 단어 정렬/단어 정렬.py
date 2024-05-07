import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())
arr = sorted(set(arr), key=lambda x: (len(x), x))
for i in range(len(arr)):
    print(arr[i])