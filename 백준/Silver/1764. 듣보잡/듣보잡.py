import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
set1 = set()
set2 = set()
for _ in range(n):
    set1.add(input().strip())
for _ in range(m):
    set2.add(input().strip())
set3 = set1 & set2
arr = sorted(list(set3))
num = len(arr)
print(num)
for i in range(num):
    print(arr[i])