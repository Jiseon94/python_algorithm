def solution(arr, query):
    # q가 2 이상일때,
    for i in range(len(query)):
        n = query[i]
        
        if (i==0):
            arr = arr[:n+1]
        if (i%2!=0):
            arr = arr[n:]
        elif (i%2 ==0):
            arr = arr[:n+1]
    return arr
        