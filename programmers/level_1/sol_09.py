

# 1. input : 정수x , 자연수 n
# 2. for i in n :
#     x +=x
#     answer.append(x)


def solution(x, n):
    answer = []
    for i in range(1, n+1):
        sum = x*i
        answer.append(sum)
    return answer

solution(4, 3)