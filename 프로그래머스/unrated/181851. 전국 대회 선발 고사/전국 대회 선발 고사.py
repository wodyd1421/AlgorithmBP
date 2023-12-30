def solution(rank, attendance):
    l = sorted([(i, x * (-int(attendance[i]) * 99 + 100)) for i, x in enumerate(rank)], key = lambda x: x[1])
    return 10000 * l[0][0] + 100 * l[1][0] + l[2][0]