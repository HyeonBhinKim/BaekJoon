def solution(n):
    answer = 0
    if n == 1:
        answer = 0
    elif n%2 == 0:
        answer = ((n*(n+2))//4)
    else:
        answer = (((n-1)*(n+1))//4)
    return answer