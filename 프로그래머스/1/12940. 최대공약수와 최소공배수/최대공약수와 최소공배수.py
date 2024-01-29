def solution(n, m):
    answer = [] # 최대공약수, 최소 공배수
    
    
    first_lst, second_lst = [], []
    first_dict, second_dict = {}, {}
    
    num = 2
    while True:
        if n == 1:
            break
        if n % num == 0:
            n = n // num
            first_lst.append(num)
            if num in first_dict.keys():
                first_dict[num] += 1
            else:
                first_dict[num] = 1   
        else:
            num += 1
            
    num = 2
    while True:
        if m == 1:
            break
        if m % num == 0:
            m = m // num
            if num in second_dict.keys():
                second_dict[num] += 1
            else:
                second_dict[num] = 1
            second_lst.append(num)
        else:
            num += 1
    
    # 최대공약수 -> 중복되는 것
    # 최소공배수 -> 존재하는 것
    
    all_keys = set(list(first_dict.keys()) + list(second_dict.keys()))
    
    print(all_keys)
    gongbae = 1
    gongyak = 1
    
    for key in all_keys:
        data1, data2 = 0,0
        if key in first_dict.keys():
            data1 = first_dict[key]
        if key in second_dict.keys():
            data2 = second_dict[key]
            
        data_max =  max(data1, data2)
        data_min = min(data1, data2)
        gongbae *= key ** data_max
        gongyak *= key ** data_min
        
    answer.append(gongyak)
    answer.append(gongbae)
                
    
    return answer 