from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    answer = 0
    dr = [-1, 1, 0, 0]
    dc = [0,0,-1,1]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    que = deque()
    que.append((0,0))
    
    while que:
        curr = que.popleft()
        for i in range(4):
            nr = curr[0] + dr[i]
            nc = curr[1] + dc[i]
            
            if nr >= n or nc >= m or nr < 0 or nc < 0 or maps[nr][nc] == 0 or visited[nr][nc] != 0:
                # print(nr, nc, "는 안 됨.")
                continue
            
            que.append((nr,nc))
            # print(nr, nc, "는 됨.")
            visited[nr][nc] = visited[curr[0]][curr[1]] + 1
            if nr == n-1 and nc == m-1:
                # print("와 드디어 끝")
                return visited[n-1][m-1]
            
            
    print(visited)
    return -1