def solution(rny_string):
    return ''.join(list(map(lambda x: 'rn' if x == 'm' else x, rny_string)))