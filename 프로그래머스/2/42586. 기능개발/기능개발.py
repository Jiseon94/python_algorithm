def solution(progresses, speeds):
    answer = []

    while progresses:
        d = (100 - progresses[0]) % speeds[0]
        num = 0
        if d != 0:
            num = (100 - progresses[0]) // speeds[0] + 1
        else:
            num = (100 - progresses[0]) // speeds[0]


        speed_plus = [i * num for i in speeds]
        progresses_plus = [i + j for i,j in zip(progresses, speed_plus)] # [100>=, 109, 23,89, 102 ....]

        print(progresses_plus)
        answer_num = 0
        for data in progresses_plus:
            if data >= 100:
                answer_num += 1
            else:
                break

        print("hi")
        print(answer_num)
        for _ in range(answer_num):
            speeds.pop(0)
            progresses.pop(0)

        print(answer_num)
        answer.append(answer_num)
    print(answer)
    return answer
