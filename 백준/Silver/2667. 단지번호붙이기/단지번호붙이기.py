# 입력
N = int(input()) # 가로 세로 길이
board = [list(map(int, input().strip())) for _ in range(N)]
# 전역변수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
house_count_list = list()
danji_count = 0

# dfs
def dfs(i, j):
    global house_count
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] != 1: continue
        board[nr][nc] = 0
        house_count += 1
        dfs(nr, nc)

# main
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            danji_count += 1
            house_count = 1
            board[i][j] = 0
            dfs(i,j)
            house_count_list.append(house_count)

print(danji_count)
house_count_list.sort()
for num in house_count_list:
    print(num)



