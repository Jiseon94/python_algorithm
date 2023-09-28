import math
def solution(n):
    #제곱근 구하기
    res = math.sqrt(n)
    print(res.is_integer())
    #정수 판별하기
    if res.is_integer() :
        return (int(res)+1)*(int(res)+1)
    return -1

print(solution(9))