def solution(board, k):
    sum = 0
    for i in range(k+1):
        for j in range(k-i+1):
            try:
                sum += board[i][j]
            except IndexError:
                pass
    return sum