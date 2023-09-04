n = int(input())
ans = [0]*n
A = list(map(int, input().split()))
stack = []
for i in range(n):
    length = len(stack)
    for j in range(length):
        if A[stack[length-j-1]] < A[i]:
            ans[stack[length-j-1]] = A[i]
            del stack[length-j-1]
        else:
            break
    stack.append(i)
for x in stack:
    ans[x] = -1
for x in ans:
    print(x, end=' ')