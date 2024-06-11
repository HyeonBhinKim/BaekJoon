def solution(sizes):
    w = 0
    h = 0
    for i in sizes:
        if max(i) > w:
            w = max(i)
        if min(i) > h:
            h = min(i)
    return w * h