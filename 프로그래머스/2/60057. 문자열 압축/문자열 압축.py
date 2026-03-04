from collections import deque
def solution(s):
    answer = 1001
    
    for i in range(1,len(s) + 1):
        length = 0                  # i 크기로 잘랐을 때 총 길이
        result = ""                 # i 크기로 잘랐을 때 완성된 문자열
        curr_alfa = ""              # 현재 알파벳 조각
        alfa_count = 1              # 현재 알파벳 조각 몇 연속인지 
        p = deque()                 # i 크기로 잘린 알파벳 조각들 넣은 큐
        
        for j in range(0,len(s),i):
            p.append(s[j:j+i])
    
        curr_alfa = p.popleft()
        
        while p:
            next_alfa = p.popleft()
            if curr_alfa == next_alfa:
                alfa_count += 1
                continue
            else: 
                result += curr_alfa
                if alfa_count != 1:
                    result += str(alfa_count)
                
                curr_alfa = next_alfa
                alfa_count = 1

        result += curr_alfa
        
        if alfa_count != 1:
            result += str(alfa_count)  
            
        length = len(result)
        
        if length < answer:
            answer = length
             
    return answer