def solution(date1, date2):
    return int(sorted((date1, date2), key = lambda x: (x[0], x[1], x[2]))[0] != date2)