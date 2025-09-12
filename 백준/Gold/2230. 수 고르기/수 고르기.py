N,M = map(int,input().split())


arr = list()
for i in range(N):
    arr.append(int(input()))

arr.sort()

L = 0
R = 0
min_gap = 2000000001

while 1:
    R += 1
    # if arr[R] - arr[L] < M:
        # print("아직 갭이 부족해: " , arr[R] - arr[L] )

    if arr[R] - arr[L] >= M:
        min_gap = min(min_gap, arr[R] - arr[L])
        # print("갭이 충분하군! 새로운 min_gap:", arr[R] - arr[L])
        L += 1
        R -= 1

    if min_gap == M:
        # print("갭이 m과 같음")
        break

    if arr[R] == arr[N - 1]:
        # print("끝까지 갔다:" , arr[R])
        break




print(min_gap)