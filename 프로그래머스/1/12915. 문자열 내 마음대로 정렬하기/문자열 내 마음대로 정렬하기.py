def solution(strings, n):
    answer = []
    e =[]
    # idx 별 원소 확인
    for string in strings:
        print(string[n])
        e.append([string[n], string])
    
    temp = sorted(e)
    # print(sorted(e))
    print(temp)
    for i in temp:
        print(i[1])
        answer.append(i[1])

    return answer