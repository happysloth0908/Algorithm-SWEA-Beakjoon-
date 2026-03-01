def solution(n):
    pibo = [0] * 100001
    pibo[0], pibo[1] = 0, 1
    
    for i in range(2,n + 1):
        pibo[i] = pibo[i-1] + pibo[i-2]
        
    return pibo[n]%1234567