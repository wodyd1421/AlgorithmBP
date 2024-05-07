import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
    if order[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    if order[0] == 'size':
        print(len(stack))
    if order[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    if order[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])