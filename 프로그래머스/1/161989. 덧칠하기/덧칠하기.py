def solution(n, m, section):
    answer = 0
    if m == 1:
        return len(section)
    else:
        tmp = 0
        for i in section:
            if tmp < i:
                tmp = i + m -1
                answer += 1
    return answer