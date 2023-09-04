import sys
input = sys.stdin.readline
n, m = map(int, input().split())
inputList = list(map(int, input().split()))
inputList.insert(0, 0)
sumList = [0]*(n+1)
resList = [0]*m
for i in range(1, n+1):
    sumList[i] = (sumList[i-1] + inputList[i]) % m
for i in range(n+1):
    resList[sumList[i]] += 1
count = 0
for i in range(m):
    count += resList[i] * (resList[i]-1) // 2
print(count)