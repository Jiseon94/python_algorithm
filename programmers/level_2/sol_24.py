def solution(s):
    print(s)
    #1. 공백을 기준으로 token을 나눈다.
    res = s.split(' ')
    print(res, type(res))
    arr = []
    #2. list를 int형으로 반환시킨다.
    for i in res:
        arr.append(int(i))
        print(arr, type(arr))
    #3. max, min으로 최소값, 최대값을 구한다.
    print(min(arr), max(arr))
    answer = str(min(arr))+' '+str(max(arr))
    print(answer)
    return answer

s = "1 2 3 4"

solution(s)