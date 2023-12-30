def solution(myString):
    s = list(myString)
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] = s[i].upper()
        if s[i] != 'A' and s[i].isupper():
            s[i] = s[i].lower()
    return ''.join(s)