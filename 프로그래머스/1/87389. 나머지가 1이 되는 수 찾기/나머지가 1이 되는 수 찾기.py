def solution(n):
    answer = 0
    while answer != n:
        answer += 1
        if n % answer == 1:
            return answer
    