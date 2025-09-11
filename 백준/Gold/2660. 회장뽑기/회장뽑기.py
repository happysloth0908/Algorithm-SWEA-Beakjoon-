from collections import defaultdict, deque


def bfs(i):
    # print("start bfs:" , i)
    que = deque(list())
    que.append([i, 0]) # 현재 좌표, 합계
    visited = list()
    visited.append(i)
    max_sum = 0

    while que:
        curr = que.popleft()
        # print("curr:" , curr)
        position = curr[0]
        summ = curr[1] + 1

        for dot in graph[position]:
            if dot not in visited:
                if max_sum < summ : max_sum = summ
                # print("max_sum 바뀌었다: ", max_sum)
                que.append([dot, summ])
                visited.append(dot)

    return max_sum

N = int(input())

graph = defaultdict(list)

while True:
    a,b = map(int, input().split())

    if a == -1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)

# print(graph)

max_friends = 0
king_list = list()

king_sum = 999
for i in graph:
    # print("i:", i)
    result = bfs(i)
    # print("result", result)
    if result < king_sum :
        king_sum = result
        king_list = []
        king_list.append(i)
    elif result == king_sum:
        king_list.append(i)

king_list.sort()

print(king_sum, len(king_list))
for i in range(len(king_list)):
    if i == len(king_list) - 1:
        print(king_list[i], end = "")
    else:
        print(king_list[i], end = " ")
