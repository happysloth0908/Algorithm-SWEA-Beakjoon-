from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    r = list([-1, 1, 0, 0]) #상하좌우
    c = list([0, 0 , -1, 1])
    
    que = deque()
    que.append((0,0,1))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while que:
        curr = que.popleft()
        cr = curr[0]
        cn = curr[1]
        csum = curr[2] 
    
        for i in range(4):
            nr = cr + r[i]
            nc = cn + c[i]
            
            if nr >= n or nc >= m or nr < 0 or nc < 0 or visited[nr][nc] or maps[nr][nc] == 0: 
                continue
            

            if nr == (n - 1) and nc == (m - 1):
                return csum + 1
            que.append((nr, nc, csum + 1))
            visited[nr][nc] = 1
            
            
   
    return -1