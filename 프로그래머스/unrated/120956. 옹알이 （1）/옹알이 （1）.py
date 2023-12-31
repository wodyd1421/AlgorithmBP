def solution(babbling):
    answer = 0
    for bab in babbling:
        count = 0
        if 'aya' in bab:
            count += 3
        if 'ye' in bab:
            count += 2
        if 'woo' in bab:
            count += 3
        if 'ma' in bab:
            count += 2
        if len(bab) == count:
            answer += 1
    return answer