def solution(citations):
    for i in range(len(citations)):
        if sorted(citations, reverse=True)[i] < i+1:
            return i
    return len(citations)