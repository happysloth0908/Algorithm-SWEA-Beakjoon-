import heapq
from sys import stdin

left, right = [],[]

N = int(stdin.readline())

for _ in range(N):
    M = int(stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -M)
    else: heapq.heappush(right, M)

    if right and -1* left[0] > right[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)

        heapq.heappush(left, -r)
        heapq.heappush(right, -l)

    print(-1 * left[0])

