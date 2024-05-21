def solution(seoul):
    a = 0
    for i in seoul:
        if i == "Kim":
            return f"김서방은 {a}에 있다"
        a += 1
