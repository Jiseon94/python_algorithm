def solution(num):
    print('함수 호출')
    answer =''
    if num % 2 == 0:
        print("Even")
        answer = 'Even'

    else:
        print('Odd')
        answer='Odd'

    return answer

look = solution(4)
print(look)




