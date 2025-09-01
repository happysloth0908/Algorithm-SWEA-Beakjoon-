leftover = set()

for _ in range (10):
    leftover.add(int(input()) % 42)

print(len(leftover))
