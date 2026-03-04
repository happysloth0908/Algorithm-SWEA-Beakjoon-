from collections import deque
def solution(s):
    answer = 1001
    i = 1
    
    while i <= len(s):
        length = 0
        curr_alfa = ""
        result = ""
        alfa_count = 1
        p = deque()
        
        for j in range(0,len(s),i):
            p.append(s[j:j+i])
        
        curr_alfa = p.popleft()
        # print("이게 현재 조각",curr_alfa)
        while p:
            next_alfa = p.popleft()
            # print("이게 다음 조각", next_alfa)
            if curr_alfa == next_alfa:
                alfa_count += 1
                # print("같으니까 숫자 커짐!", alfa_count)
                continue
            else: 
                result += curr_alfa
                if alfa_count != 1:
                    result += str(alfa_count)
                
                curr_alfa = next_alfa
                alfa_count = 1
                # print("달라서 교체! 현재 result는",result)

        result += curr_alfa
        if alfa_count != 1:
            result += str(alfa_count)        
        length = len(result)
        if length < answer:
            answer = length
        length = 0
        i += 1
        # print("결론:", i, "로 쪼개면 결과는", result,"길이는", length )
        
        
        
        
    return answer