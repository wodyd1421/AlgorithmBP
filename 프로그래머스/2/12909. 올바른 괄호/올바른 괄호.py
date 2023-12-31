def solution(s):
    result = []
    for x in s:
        if result and result[-1] == '(' and x == ')':
            del result[-1]
        else:
            result.append(x)
    return not bool(result)