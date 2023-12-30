def solution(picture, k):
    ans = []
    for x in picture:
        str = ''
        for y in x:
            if y == 'x':
                str += 'x'*k
            else:
                str += '.'*k
        ans += [str]*k
    return ans