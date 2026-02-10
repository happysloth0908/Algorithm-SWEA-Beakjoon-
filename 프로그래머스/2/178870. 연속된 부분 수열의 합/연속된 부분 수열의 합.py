# 비내림차순이란..? 감소하지 않게 정렬된거..! 중복 있음. 
def solution(sequence, k):
    # sequence.sort() #할 필요 없음... 
    
    length = len(sequence) #O(n)
    r = 0
    l = 0
    current_sum = sequence[0]
    width = 1000000000
    ans_r = 0
    ans_l = 0
    while l < length and r < length: 
        if current_sum < k:
            
            r += 1 
            if r == length: break
            current_sum += sequence[r]
        elif current_sum > k:
            current_sum -= sequence[l] 
            l += 1
            # print(l,r)
            
        elif current_sum == k:
            s = r - l
            if s < width:
                width = s
                ans_r = r
                ans_l = l
            if width == 0:
                print(ans_l,ans_r)
                return list([ans_l,ans_r])
            r += 1
            if r == length: break
            current_sum += sequence[r]
    
            
    return list([ans_l,ans_r])