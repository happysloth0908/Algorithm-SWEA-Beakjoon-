def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        cut = array[i -1: j ]
        print(cut)
        cut.sort()
        ans = cut[k - 1]
        answer.append(ans)
        
    return answer