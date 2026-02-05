def solution(t, p):
    answer = 0
    int_p = int(p)
    
    for i in range(len(t)):
        summ = ""
        for j in range(len(p)):
            if i + j < len(t):
                summ += t[i + j]
                # print( i+ j , "번째 숫자 더하면", summ)
            else: return answer
        if int(summ) <= int_p: 
            answer += 1
            print("이제 답은 ", answer)
        
            

    return answer