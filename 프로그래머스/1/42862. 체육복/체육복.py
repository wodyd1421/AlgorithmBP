def solution(n, lost, reserve):
    count = 0
    lenLost = len(lost)
    lost.sort()
    reserve.sort()
    for elem in set(lost) & set(reserve):
        lost.remove(elem)
        reserve.remove(elem)
        count += 1
    while lost and reserve:
        if reserve[0] < lost[0] - 1:
            del reserve[0]
        elif lost[0] < reserve[0] - 1:
            del lost[0]
        else:
            count += 1
            del lost[0]
            del reserve[0]
    return n - lenLost + count