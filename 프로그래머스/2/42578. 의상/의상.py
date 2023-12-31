def solution(clothes):
    a = dict()
    ans = 1
    for x, y in clothes:
        if y in a:
            a[y] += 1
        else:
            a[y] = 1
    for x in a.values():
        ans *= x+1
    return ans-1