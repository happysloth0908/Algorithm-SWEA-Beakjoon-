import sys
# from collections import dict

nr = [0, 1, 1, 1, 0, -1, -1, -1]
nc = [-1, -1, 0, 1, 1, 1, 0, -1]


input = sys.stdin.readline() # readline 뒤에 꼭 ()

N, M , K = map(int, input.split()) #split 해줘야 함.

# print(N,M,K)

arr = [[0 for _ in range(M)] for _ in range(N) ]
# print(arr)


for i in range(N):
    tmp = sys.stdin.readline().strip()
    # print(len(tmp))
    for j in range(len(tmp)):
        arr[i][j] = tmp[j]

gods_arr = []
ans_list = dict()

for i in range(K):
    tmp = sys.stdin.readline().strip()
    gods_arr.append(tmp)
    ans_list[tmp] = 0


def dfs(string, arr, x, y, depth):
    # print("----현재 위치:----" , x, y)
    # print("depth:", depth)

    # if arr[x][y] != word[depth]: # 🚨 이거 안 했었음... 그래서 단어가 아님에도 불구하고 계속 탐색함. 무한 재귀
    #     return
        # print("현재 있는 단어는", depth ," 번째인 ", word[depth])

    if string in gods_arr:
        # print(string , " 은 목록에 있다! 추가함")
        ans_list[string] += 1
        return

    depth += 1

    if depth >= 5:
        # print("현재 ans는" , ans)
        return

    # 8방 탐색 후 / 삐져나오는 애들 정리 / word 의 다음 알파벳이면 가기 ... 현재가 어딘지 그 뒤가 뭔지 알아야 함...
    for i in range(8):
        nx = x + nr[i]
        ny = y + nc[i] #🚨 y를 x 로 씀. 나 이거 자주 실수함.

        # print("다듬기 전 x,y: " , nx, ny)

        if nx < 0: nx = N - 1
        elif nx >= N: nx = 0

        if ny < 0: ny = M - 1
        elif ny >= M: ny = 0

        # print("다듬기 후 x,y: " , nx, ny)
        # print(string)
        dfs(string + arr[nx][ny] , arr, nx , ny,  depth)
        # print(string)



for i in range(N):
    for j in range(M):
        dfs(arr[i][j],arr, i, j, 0)

for ans in list(ans_list.values()):
    print(ans)



