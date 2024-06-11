def solution(t, p):
    answer = 0
    p_length = len(p)
    p_num = int(p)
    count = 0

    for i in range(len(t) - p_length + 1):
        sub_num = int(t[i:i + p_length])
        if sub_num <= p_num:
            answer += 1
    
    return answer