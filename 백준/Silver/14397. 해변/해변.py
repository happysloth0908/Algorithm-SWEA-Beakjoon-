# 홀수
odd_x = [1, -1, 0, 0, 1, -1]
odd_y = [0, 0, -1, 1, 1, 1]
# 짝수
even_x = [1, -1, 0, 0, 1, -1]
even_y = [0, 0, -1, 1, -1, -1]

N, M = map( int, (input().split()))

grid = [ list(input().strip()) for _ in range(N) ]
# print(grid)
count = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == "#":
            if i % 2 == 1: # 홀수면
                odd_or_even = odd_x, odd_y
            else:
                odd_or_even = even_x, even_y

            for k in range(len(odd_x)):
                new_x = i + odd_or_even[0][k]
                new_y = j + odd_or_even[1][k]
                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M and grid[new_x][new_y] == ".":
                    count += 1

print(count)


