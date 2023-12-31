def solution(participant, completion):
    d = dict()
    for x in participant:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for x in completion:
        d[x] -= 1
    return [x for x in d if d[x] == 1][0]