def solution(d, budget):
    #신청한 금액 총합 확인하기
    sum = 0
    for b in d:
        sum +=b
        print(sum)
    print(sum)
    #전체 예산과 같거나 작다면 d[]개수 뽑으면 됨.
    #전체 예산보다 많다면, 가장 많은 조합의 합을 찾아야함.
    if sum > budget:
        print('예산초과')
        #최소예산끼리의 조합을 찾는 방법?
        com = 0
        while com<=budget:
            cnt = 0
            for i in d:
                print(com)
                com +=i
                print(com, budget)
                cnt +=1
            break
    answer = 0
    print(cnt)
    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))

