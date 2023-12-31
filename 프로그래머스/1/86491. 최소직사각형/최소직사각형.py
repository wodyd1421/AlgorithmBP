def solution(sizes):
    m = []
    n = []
    for i in range(len(sizes)):
        m.append(sizes[i][0])
        m.append(sizes[i][1])
        n.append(min(sizes[i]))
    width = max(m)
    height = max(n)
    return width * height