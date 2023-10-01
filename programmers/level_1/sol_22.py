def solution(sizes):
    max = 0 #가로 세로중 가장 큰 수
    min = 0 #가로 세로중 가장 작은 수
    max_arr = []
    min_arr = [] #가로 세로 중 가장 작은 수끼리 모은거
    for i in range(len(sizes)):
        # 2차원배열안의 요소를 순서대로 정렬해주었다.
        sizes[i].sort()
        # print(sizes)
        #각 배열 중 가장 큰 수를 뽑았다.  ->가로
        max_arr.append(sizes[i][-1])
        max_arr.sort()
        max = max_arr[-1]
        print(max)

        min_arr.append(sizes[i][0])
        min_arr.sort()

        min = min_arr[-1]
        print(min)
    print('max:', max)
    print('min:', min)

    answer = max*min

    return answer

sizes= [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))