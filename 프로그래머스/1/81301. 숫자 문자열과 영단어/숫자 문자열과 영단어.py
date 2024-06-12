def solution(s):
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    result = []
    temp = ""
    
    for char in s:
        temp += char
        if temp in num_dict:
            result.append(num_dict[temp])
            temp = ""
        elif temp.isdigit():
            result.append(temp)
            temp = ""
    answer = ''.join(result)
    
    return int(answer)