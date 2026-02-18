from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0,0,-1,1]
    
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    
    que = deque()
    que.append((0,0))
    
    while que:
        r,c = que.popleft()
        if r == n-1 and c == m-1:
            return visited[n-1][m-1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr >= n or nc >= m or nr < 0 or nc < 0 or maps[nr][nc] == 0 or visited[nr][nc] != 0:
                continue
            
            que.append((nr,nc))
            visited[nr][nc] = visited[r][c] + 1
    return -1