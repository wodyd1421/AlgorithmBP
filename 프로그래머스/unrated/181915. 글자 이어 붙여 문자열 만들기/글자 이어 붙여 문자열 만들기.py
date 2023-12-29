def solution(my_string, index_list):
    answer=''
    for m in index_list:
        answer += my_string[m]
    return answer