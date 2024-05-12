import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
dic_int = dict()
dic_str = dict()
for i in range(n):
    word = input().strip()
    dic_int[i+1] = word
    dic_str[word] = i+1
for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(dic_int[int(q)])
    else:
        print(dic_str[q])