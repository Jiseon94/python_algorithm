def solution(intStrs, k, s, l):
    answer = []
    # s 값 확인하여 자르기
    for i in range(len(intStrs)):
        # print(intStrs[i][s:s+l])
        num = intStrs[i][s:s+l]
        # 대소 비교
        if(k<int(num)):
            answer.append(int(num))

    return answer