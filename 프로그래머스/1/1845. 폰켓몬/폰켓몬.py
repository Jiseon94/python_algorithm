def solution(nums):
    answer = len(nums)//2
    # 최대 많이 가질수 있는 max = nums/2

    nums.sort()
    # print(nums)
    
    dict = {}
    num_len = len(nums)
    
    for i in range(len(nums)):
        # print(nums[i])
        dict[nums[i]] = nums.count(nums[i])
        
    # print(dict)

    # 전체 길이와 dict 의 key 수 비교 : 종류 수
    # print(len(dict))
    if (num_len == len(dict)) or len(dict) >= answer:
        return answer

    if len(dict) < answer :
        return len(dict)
