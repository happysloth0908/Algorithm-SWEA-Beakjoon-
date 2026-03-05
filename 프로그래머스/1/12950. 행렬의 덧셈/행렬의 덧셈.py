def solution(arr1, arr2):
    answer = [[]]
    r = len(arr1)
    c = len(arr1[0])
    arr3 = [[0]*c for _ in range(r)]
    # print(arr3)
    for i in range(r):
        for j in range(c):
            arr3[i][j] = arr1[i][j] + arr2[i][j]
    return arr3