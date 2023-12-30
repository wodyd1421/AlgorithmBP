def solution(order):
    ans = 0
    for x in order:
        if 'caf' in x:
            ans += 5000
        else:
            ans += 4500
    return ans