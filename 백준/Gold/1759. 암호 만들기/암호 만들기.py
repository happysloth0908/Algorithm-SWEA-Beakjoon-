from itertools import permutations, combinations

L , C = map(int, input().split())
arr = list(input().split())
arr.sort()

ans = list(combinations(arr, L))

vou =  ['a', 'e', 'i', 'o', 'u']

real_ans = list()

for a in ans:
    combo = set(a)

    # print("conbo:" , combo)
    if len(combo.intersection(vou)) != 0:
        if len(combo) - len(combo.intersection(vou)) >= 2:
            tmp = list(combo)
            tmp.sort()
            real_ans.append(tmp)

for i in real_ans:
    print("".join(i))
