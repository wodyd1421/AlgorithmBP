def solution(myString, pat):
    s = ''.join(list(map(lambda x: 'A' if x == 'B' else 'B', myString)))
    return int(pat in s)