def solution(myString, pat):
    c = 0
    s = len(myString)-len(pat)+1
    while True:
        s = myString[:s+len(pat)-1].rfind(pat)
        if s == -1:
            return c
        c += 1