from collections import deque

def solution(progresses, speeds):
    l = []
    ans = []
    count = 1
    for i in range(len(speeds)):
        c = (100-progresses[i])//speeds[i]
        if (100-progresses[i])/speeds[i] == c:
            l.append(c)
        else:
            l.append(c+1)
    deq = deque(l)
    a = deq.popleft()
    while deq:
        while deq:
            b = deq.popleft()
            if a >= b:
                count += 1
            else:
                break
        ans.append(count)
        if a < b and not deq:
            ans.append(1)
        a = b
        count = 1
    return ans