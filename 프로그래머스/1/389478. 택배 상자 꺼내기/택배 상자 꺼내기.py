import math

def solution(n, w, num):
    h = math.ceil(n / w) # 높이 
    storage = []
    for i in range(h):
        row = []
        for j in range(1, w + 1):
            if (w * i + j) <= n:
                row.append(w * i + j)
            else: row.append(0)
        
        if i % 2 != 0: # 홀수면 뒤집기
            row.reverse()
        storage.append(row)
            
    
    print(storage)
    sum = 0
    curr_floor = math.ceil(num / w) - 1 #num 이 있는 층부터 시작
    for i in range(w):
        if storage[curr_floor][i] == num:
            while 1:
                curr_floor += 1 
                if curr_floor >= h or storage[curr_floor][i] == 0: break
                sum += 1
            break
                
    
    print(sum)
    answer = sum + 1
    return answer