def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        numbers = 0
        for _ in range(1, i+1):
            if i % _ == 0:
                numbers += 1
        if numbers % 2:
            answer -= i
        else:
            answer += i

    return answer