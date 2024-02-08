# def solution(array, commands):
#     answer = []
#     #공통 기능 :
#     #i ~ j 인덱스 추출
#     #sort() 정렬
#     for i in range(len(commands)):
#         k = commands[i][2]
#         num =[]
#         for j in range(0, 2):
#             num.append(commands[i][j])
#         # print(num)

#         temp = array[(num[0]-1):num[1]]
#         temp.sort()
#         # print(k)
#         # print(temp)
#         answer.append(temp[k-1])
        
        
#     return answer

def solution(array, commands):
    answer = []
    #공통 기능 :
    #i ~ j 인덱스 추출
    #sort() 정렬
    for command in commands:
        # print(command)
        i = command[0]
        j = command[1]
        k = command[2]
        print(i, j, k)
        temp = sorted(array[(i-1):j])
        answer.append(temp[(k-1)])

    return answer