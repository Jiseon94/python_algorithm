# 1. n 은 자연수
# 2. str 로 변환
# 3. str 을 거꾸로 반복해서 list에 append

def solution(n):
    answer = []
    num = str(n)
    print(num, type(num))
    for i in num[::-1]:
        answer.append(int(i))
        print(answer)
    return answer

print(solution(7364))

def solution(n):
    num = str(n)
    return [int(i) for i in num[::-1]]

print(solution(99998767))