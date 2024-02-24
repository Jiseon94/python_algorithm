# 이름 오름차순 정렬 후 풀어보기!!

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)
    
    # dict 로 풀어보기
    for c in range(0, len(completion)):
        if completion[c] == participant[c]:
            # print("같다")
            continue
        elif completion[c] != participant[c]:
            # print("다르다")
            # print(participant[c])
            return participant[c]
        
    return participant[-1]
    