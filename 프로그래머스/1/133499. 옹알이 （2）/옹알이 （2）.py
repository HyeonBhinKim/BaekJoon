# def solution(babbling):
#     answer = 0
#     cansay = ["aya", "ye", "woo", "ma"]
#     for i in babbling:
#         tmp = ''
#         said = ''
#         for j in i:
#             tmp += j
#             if tmp in cansay and tmp != said:
#                 said = tmp
#                 tmp = ''
#             if len(tmp) > 3:
#                 break
#         if tmp == '':
#             answer +=1
        
#     return answer
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer