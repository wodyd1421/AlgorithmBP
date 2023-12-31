def solution(targets):
    targets.sort(key=lambda x:x[1])
    b = [targets[0][1]-0.5]
    for a in targets:
        if b[-1] < a[0]:
             b.append(a[1]-0.5)
    return len(b)