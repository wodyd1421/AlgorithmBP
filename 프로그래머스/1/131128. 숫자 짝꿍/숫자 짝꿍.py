def solution(X, Y):
    c = []
    for n in range(10):
        c += [str(n)] * min(X.count(str(n)), Y.count(str(n)))
    if not c:
        return '-1'
    elif set(c) == set('0'):
        return '0'
    else:
        c.sort(reverse=True)
        return ''.join(c)