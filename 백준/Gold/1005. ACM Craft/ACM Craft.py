from sys import stdin
from collections import deque

T = int(stdin.readline()) #테케

for _ in range(T):

    N, K = map(int , stdin.readline().split() )#건물 개수 , 규칙 수

    time = list(map(int, stdin.readline().split())) #걸리는 시간
    adj_time = [0] * N
    adj = [0] * N # 가중치 기록
    graph = [[] for _ in range(N)]

    # 중요!!! 건물 번호에서 -1 해야 실제 배열 속 건물 값이 나옴.

    for _ in range(K):
        a, b = map(int , stdin.readline().split() )
        a -= 1
        b -= 1
        adj[b] += 1
        graph[a].append(b)

    W = int(stdin.readline()) #승리의 건물
    W -= 1

    que = deque()
    ans = 0

    dp = [0] * N

    for i in range(len(adj)):
        dp[i] = time[i]
        if adj[i] == 0:
            que.append(i)

    while que:
        curr = que.popleft()

        for child in graph[curr]:
            adj[child] -= 1
            if adj[child] == 0:
                que.append(child)
            dp[child] = max(dp[child], time[child] + dp[curr])

    print(dp[W])

