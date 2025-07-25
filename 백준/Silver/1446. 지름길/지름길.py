import sys

input = sys.stdin.readline

N, D = map(int, input().split())

# dp[i] = 위치 i까지 도달하는 최소 거리
dp = [i for i in range(D + 1)]

# 지름길 정보 저장
shortcuts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    shortcuts.append([start, end, length])

# DP 계산
for i in range(1, D + 1):
    # 이전 위치에서 1칸 이동하는 경우
    dp[i] = min(dp[i], dp[i - 1] + 1)

    # 모든 지름길을 확인하여 현재 위치로 올 수 있는지 검사
    for start, end, length in shortcuts:
        # 현재 위치가 지름길의 끝점이고, 지름길이 유효한 경우
        if end == i and start <= D:
            dp[i] = min(dp[i], dp[start] + length)

print(dp[D])