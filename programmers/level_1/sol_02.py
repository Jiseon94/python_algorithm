
# 약수 : 1, 2, 3,5, 7, 13

list =[]

def func(n):
    print('함수 호출')
    def sol(list):
        answer = 0
        for i in list:
            answer += i
        print('answer', answer)
        return answer


    for i in range(n):
        if n%(i+1) == 0:
            print(i+1)
            list.append(i+1)
    return sol(list)

func(12)
print(list)
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