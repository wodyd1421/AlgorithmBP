import re

def solution(dartResult):
    score = [0] * 3
    darts = re.findall(r'([0-9]+)([SDT])([*#]?)', dartResult)
    for idx, (num, pwr, opt) in enumerate(darts):
        score[idx] = int(num)
        if pwr == 'D':
            score[idx] **= 2
        elif pwr == 'T':
            score[idx] **= 3
        if opt == '*':
            score[idx] *= 2
            if idx >= 1:
                score[idx - 1] *= 2
        elif opt == '#':
            score[idx] *= -1
    return sum(score)