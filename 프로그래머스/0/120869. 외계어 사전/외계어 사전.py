def solution(spell, dic):
    answer = 2
    for i in range(len(dic)):
        print(dic[i])
        
        num = len(spell)
        print(num)
        
        for s in spell:
            if (s in dic[i]):
                print("있음")
            else:
                num-=1
                break
        if num == len(spell):
            answer=1
            
                
                 
    return answer