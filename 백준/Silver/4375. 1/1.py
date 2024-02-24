def fn(n):
    ct = 1
    num = 1
    while True:
        if num % n == 0:
            print(ct)
            return
        num = 10 * num + 1
        ct += 1
while True:
    try:
        n = int(input())
        fn(n)
    except:
        break