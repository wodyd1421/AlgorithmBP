n = int(input())
a = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
for i in range(m):
    print(int(check[i] in a))