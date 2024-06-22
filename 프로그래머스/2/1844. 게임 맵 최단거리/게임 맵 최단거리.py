from collections import deque

def solution(maps):
    
    answer = 0
    
    # 동서남북 방향
    dx = [-1, 1, 0, 0] #좌, 우
    dy = [0, 0, 1, -1] #상, 하
    
    queue = deque()
    queue.append((0, 0))
    
    n = len(maps) # 가로 길이
    m = len(maps[0]) #세로 길이
    
    while queue:
        x, y = queue.popleft()
        
        #상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >=m :
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    answer = maps[n-1][m-1]
    if answer <= 1:
        return -1
    
    return answer