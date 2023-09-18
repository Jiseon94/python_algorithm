# 1. n%a == 1
# 2. a를 for문으로 하나씩 대입
# 3. 가장 작은 a 를 도출


answer = 0
def solution(n):
    for a in range(1, n + 1)[::-1]:
        if (n % a) == 1:
            answer = a
        else:
            pass
    return answer

print(solution(10))
