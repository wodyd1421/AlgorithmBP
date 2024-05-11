import sys
input = sys.stdin.readline
s = set()
m = int(input())
for _ in range(m):
    a = input().split()
    if a[0] == 'add':
        s.add(int(a[1]))
    if a[0] == 'remove':
        if int(a[1]) in s:
            s.remove(int(a[1]))
    if a[0] == 'check':
        print(int(int(a[1]) in s))
    if a[0] == 'toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    if a[0] == 'all':
        s = set(range(1, 21))
    if a[0] == 'empty':
        s = set()