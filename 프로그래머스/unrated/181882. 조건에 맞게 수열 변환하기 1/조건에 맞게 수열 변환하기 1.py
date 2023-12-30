def solution(arr):
    a = []
    for c in arr:
        if c % 2 and c < 50:
            a += [2 * c]
        elif not c % 2 and c >= 50:
            a += [c / 2]
        else:
            a += [c]
    return a