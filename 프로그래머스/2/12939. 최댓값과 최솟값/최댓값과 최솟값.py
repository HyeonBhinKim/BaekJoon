def solution(s):
    arr = list(map(int, s.split()))
    answer = [min(arr),max(arr)]
    return ' '.join(map(str, answer))