# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c

N, d, k, c = map(int, input().split())
belt = []

for _ in range(N):
    belt.append(int(input()))

ans = 0

if N == k:  # 전체 초밥 수와 연속해서 먹어야 하는 수가 같으면
    if c in belt:
        ans = d # 전체 초밥의 가짓수가 답..
    else:
        ans = d + 1

final_set = set()

for i in range(N):
    tmp = set()
    for j in range(k):
        tmp.add(belt[(i + j ) % N])

    tmp.add(c)
    if len(final_set ) < len(tmp):
        final_set = tmp



print(len(final_set))