from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 간선 수

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
que = deque([1])
while que:
   p =  que.popleft()
   for c in graph[p]:
       if visited[c] == 0:
           que.append(c)
           visited[c] = 1

print(sum(visited) -1)



