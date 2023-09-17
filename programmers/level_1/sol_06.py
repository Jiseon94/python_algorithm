import math



def solution(n):
    answer = 0
    res = list(str(n))  # 숫자를 하나씩 떼어서 문자로 저장
    # print(res, type(res))

    for i in range(0, len(res)):
        answer += int(res[i])
        # print(answer, type(answer))

    # result = answer
    return answer


print(solution(123))

# number = 1435
#
# res = list(str(number)) #숫자를 하나씩 떼어서 문자로 저장
# print(res, type(res))
#
# sum =0
# for i in range(0, len(res)):
#     sum +=int(res[i])
#     print(sum, type(sum))