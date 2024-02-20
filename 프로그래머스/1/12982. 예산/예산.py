def solution(d, budget):
    d.sort()
    money = 0
    for i in range(len(d)):
        money += d[i]
        if money > budget:
            return i
    return len(d)