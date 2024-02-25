while True:
    n = int(input())
    if n == 0:
        break
    book = [0] * (n+1)
    arr = input().split(',')
    for m in arr:
        try:
            low = m.split('-')[0]
            high = m.split('-')[1]
        except:
            low = m
            high = m
        for i in range(int(low), int(high)+1):
            if i <= n:
                book[i] = 1
    print(book.count(1))