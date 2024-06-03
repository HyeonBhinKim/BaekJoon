def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        money -= i*price
    if money < 0:
        return -1*money
    else:
        return answer