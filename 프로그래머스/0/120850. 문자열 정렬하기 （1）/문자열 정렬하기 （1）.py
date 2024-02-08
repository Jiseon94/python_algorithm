def solution(my_string):
    answer = []
    temp = []
    for char in my_string:
        if char.isdigit():
            temp.append(int(char))

    end = len(temp)
    # print(end)
    answer = [0 for i in range(end)] # list 길이 지정!!!!
    # print(answer)
    
    print(temp)
    temp.sort()
    print(temp)
#     lst = []
#     while temp:
#         num = min(temp)
#         lst.append(num)
#         idx = temp.index(num)
#         temp.pop(idx)
    
#     print(lst)

    return temp