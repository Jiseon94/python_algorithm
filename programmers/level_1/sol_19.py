def solution(arr):
    answer = []
    # print(arr)

    #배열 요소 하나씩 꺼내어 바로 앞 전꺼랑 비교
    for a in range(len(arr)):
        print(arr[a])
        answer.append(arr[a])
        print(answer)

    return answer

arr = [1,1,3,3,0,1,1]
# print(solution(arr))
solution(arr)