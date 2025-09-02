
from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = []

for _ in range(N):
    belt.append(int(input()))

window = defaultdict(int)

for i in range(k):
    window[belt[i]] += 1

window[c] += 1

ans = len(window)

for i in range(0,N - 1):
    window[belt[i]] -= 1
    if window[belt[i]] == 0:
        del window[belt[i]]
    window[belt[(k + i) % N]] += 1
    ans = max(ans, len(window))

print(ans)


