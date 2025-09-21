from sys import stdin
import heapq
from collections import defaultdict

N = int(stdin.readline())

max_tree = [] # 가장 큰 것부터 위에
min_tree = [] # 가장 작은 것부터 위에
problems = defaultdict() #넣은 문제들 정렬은 안 함.

for _ in range(N):
    p , l = map(int, stdin.readline().split() )
    problems[p] = l
    heapq.heappush(min_tree, (l, p))
    heapq.heappush(max_tree, (-l, -p))


# print(max_tree)
# print(min_tree)

M = int(stdin.readline())
for _ in range(M):
    tmp = list(stdin.readline().split())
    if tmp[0] == "add":
        problems[int(tmp[1])] = int(tmp[2])
        heapq.heappush(min_tree, (int(tmp[2]), int(tmp[1])))
        heapq.heappush(max_tree, (-1 * int(tmp[2]), -1 * int(tmp[1])))
        # print("추가된 후 max:", max_tree)
        # print("추가된 후 min :", min_tree)
        # print("추가된 후 problems :", problems)



    elif tmp[0] == "recommend":
        if int(tmp[1]) == 1:
            if problems.get(-1 * max_tree[0][1], None) != -1 * max_tree[0][0]:
                # print("삭제된게 있다! :", -1 *  max_tree[0][1], "번 문제", -1 * max_tree[0][0])
                heapq.heappop(max_tree)


            print(-1 * max_tree[0][1])


        else:
            if problems.get(min_tree[0][1], None) != min_tree[0][0]:
                # print("삭제된게 있다!")
                heapq.heappop(min_tree)
            print(min_tree[0][1])
    elif tmp[0] == "solved":
        problems.pop(int(tmp[1]))


