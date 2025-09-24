from sys import stdin

N = int(stdin.readline())
parent = [] * N

for i in range(N):
    parent.append(i)

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    ap = find_parent(a)
    bp = find_parent(b)
    if ap != bp:
        if ap < bp:
            parent[bp] = ap
        else: parent[ap] = bp

all_lines = [] # ( 비용, a, b)

for i in range(N):
    tmp = list(map(int, stdin.readline().split()))
    for j in range(i + 1, N):
        all_lines.append((tmp[j], i, j))

all_lines.sort()
ans = 0

for i in range(len(all_lines)):
    a = all_lines[i][1]
    b = all_lines[i][2]
    if find_parent(a) != find_parent(b):
        union(a, b)
        ans += all_lines[i][0]


print(ans)
