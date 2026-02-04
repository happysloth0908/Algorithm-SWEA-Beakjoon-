# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i = command[0]
#         j = command[1]
#         k = command[2]
        
#         cut = array[i -1: j ]
#         print(cut)
#         cut.sort()
#         ans = cut[k - 1]
#         answer.append(ans)
        
#     return answer

1
2
3
4
5
6
7
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer