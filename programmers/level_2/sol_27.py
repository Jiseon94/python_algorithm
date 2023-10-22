def solution(s):

    s = s.lower()
    jaden = s.split(" ")

    answer = ''
    result = []
    for i in range(len(jaden)):
        result.append(jaden[i][0].upper()+jaden[i][1:])
        answer=' '.join(result)
    print(answer)

    return answer

s = "3people unFollowed me"

# print(solution(s))
solution(s)