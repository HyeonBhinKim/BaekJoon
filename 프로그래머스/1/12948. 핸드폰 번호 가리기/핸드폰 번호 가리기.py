def solution(phone_number):
    length = len(phone_number)
    answer = '*' * (length-4)
    
    return answer + phone_number[-4:]