
# 약수 : 1, 2, 3,5, 7, 13



def solution(n):
    print('함수 호출')
    def sol(divisors):
        answer = 0
        for i in divisors:
            answer += i
        print('answer', answer)
        return answer

    divisors = []
    for i in range(n):
        if n%(i+1) == 0:
            print(i+1)
            divisors.append(i+1)

    result = sol(divisors)
    return result
print(solution(12))
# print(list)
# def sol(list):
#     answer = 0
#     for i in list:
#         answer+=i
#     print(answer)
#     return answer

# sol(list)



# def solution(n):
#     print('함수 호출')
#     answer = 0
#     for i in range(n):
#         print('n', n, 'i',i)
#         div = []
#         if (n%(i+1) == 0):
#             div.append(i)
#             return div
#         else:
#             return div
#         print(div)
#         for j in div:
#             answer+= j
#     return answer
#
# solution(12)

# print(12/2)
# print(12//2)
# print(12%2)
# print(12%5)

# div = []
# div.append(4)
# div.append(9)
# print(div)

# def func(n):
#     print('함수 호출')
#     def sol(divisors):
#         answer = 0
#         for i in divisors:
#             answer += i
#         print('answer', answer)
#         return answer
#
#     divisors = []  # 리스트 이름을 변경
#     for i in range(n):
#         if n % (i + 1) == 0:
#             print(i + 1)
#             divisors.append(i + 1)
#
#     result = sol(divisors)  # sol 함수를 호출하고 반환값을 저장
#     return result
#
# # n = 12  # 예제에서는 n을 12로 설정
# print(func(12))