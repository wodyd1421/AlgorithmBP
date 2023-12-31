def solution(number, k):
    ret = ''
    ln = len(number)
    for i in range(ln - k):
        idx, mx = 0, number[0]
        for j in range(9, 0, -1):
            try:
                c = number[:len(number) - ln + k + 1].index(str(j))
                idx = c
                mx = str(j)
                break
            except:
                pass
        ret += mx
        number = number[idx + 1:]
        k += 1
    return ret