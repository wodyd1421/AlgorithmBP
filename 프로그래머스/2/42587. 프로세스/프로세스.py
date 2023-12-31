def solution(priorities, location):
    count = 0
    for n in range(9,0,-1):
        try:
            while True:
                idx = priorities.index(n)
                if idx == location:
                    return count+1
                priorities = priorities[idx+1:] + priorities[:idx]
                count += 1
                location = (location-idx+len(priorities))%(len(priorities)+1)
        except:
            pass
        