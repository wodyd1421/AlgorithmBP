n = int(input())
for i in range(5):
    if n - 3 * i < 0:
        print(-1)
        break
    elif (n-3*i) % 5 == 0:
        print((n-3*i)//5+i)
        break