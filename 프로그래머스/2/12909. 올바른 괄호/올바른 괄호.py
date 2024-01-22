def solution(s):
    answer = list()
    sum = 0
    for i in range(len(s)):
        answer.append(s[i])

    if (answer[0] == "(" and answer[-1] ==")") and answer.count("(") == answer.count(")") :
        for i in range(len(answer)):
            if answer[i] =="(" :
                sum+=1
            else:
                sum-=1
            if sum <0 :
                print("F")
                return False
        print("True")
        return True
    print("F")
    return False