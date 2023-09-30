def solution(d, budget):
    com = 0 #최대의 조합
    answer = 0 #몇 개 부서까지 지원가능한지
    b = d
    b.sort()
    for i in b:
        com += i
        answer +=1
        print('c:', answer, 'com:', com)
        if com > budget:
            print('초과')
            answer -= 1
            print(answer)
            break
        elif com == budget:
            print('같다:', answer)
            break
    return answer

d = [2000,2,3,3]
budget = 10
# print(solution(d,budget))
solution(d,budget)
