t = int(input())
for _ in range(t):
    r, s = input().split()
    p = ''
    for i in range(len(s)):
        p += s[i]*int(r)
    print(p)