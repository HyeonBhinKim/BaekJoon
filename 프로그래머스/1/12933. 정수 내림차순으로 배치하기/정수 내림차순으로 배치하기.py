def solution(n):
    numbers = [int(i) for i in str(n)]
    numbers = sorted(numbers, reverse=True)
    answer = int(''.join(map(str, numbers)))
    return answer