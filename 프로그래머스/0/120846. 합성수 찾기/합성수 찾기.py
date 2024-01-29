def solution(n):
    answer=0
    num = list()
    for i in range(n):
        i+=1
        if (i>3):
            num.append(i)
    # print(num)
    
    for i in range(len(num)):
        # print(num[i])
        for j in range(2,num[i]):
            if(num[i]%j == 0):
                answer+=1
                print(num[i])
                print(j)
                print("합성수")
                break

    return answer