def solution(arr):
    answer = []
    #우선 배열의 0번째 idx 넣기
    answer.append(arr[0])
    # print(answer)

    # 배열 요소 하나씩 꺼내어보기
    for a in range(len(arr)):
        if answer[-1] == arr[a]:
            print(a+1,'번째 : 앞에꺼랑 같다')
            print('answer[-1] : ', answer[-1], '/ arr[a]:', arr[a])
            continue
        else:
            print(a+1,'번째 : 다르군')
            print('answer[-1] : ', answer[-1], '/ arr[a]:', arr[a])
            # 꺼낸 배열 요소를 answer arr에 넣기
            answer.append(arr[a])

    print(answer)

    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
solution(arr)