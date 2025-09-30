from sys import stdin
from collections import deque
from itertools import combinations
import copy

N,M = map(int, stdin.readline().split())

lab = []

for _ in range(N):
    lab.append(list(map(int, stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque()

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                que.append((i,j))

    infected_lab = [row[:] for row in lab]

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or ny >= M or nx < 0 or ny < 0 : continue
            if infected_lab[nx][ny] == 0:
                infected_lab[nx][ny] = 2
                que.append((nx,ny))

    cnt = sum(row.count(0) for row in infected_lab)
    global answer
    answer = max(answer, cnt)

# def wall(cnt):
#
#     if cnt >= 3:
#         bfs()
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j] == 0:
#                 lab[i][j] = 1
#                 wall(cnt + 1)
#                 lab[i][j] = 0
answer = 0

blanks = []

for i in range(N):
    for j in range(M):
      if lab[i][j] == 0:
          blanks.append((i,j))

for (x,y), (x2, y2), (x3, y3) in combinations(blanks, 3):
    lab[x][y] = 1
    lab[x2][y2] = 1
    lab[x3][y3] = 1
    bfs()
    lab[x][y] = 0
    lab[x2][y2] = 0
    lab[x3][y3] = 0




print(answer)