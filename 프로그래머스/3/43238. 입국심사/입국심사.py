def test(mid,n,times): #되나? 확인
    sum = 0
    for time in times:
        sum += mid // time
    # print("sum은",sum)
    if sum >= n:
        return True
    elif sum < n:
        return False
    
    
def solution(n, times):
    times.sort() # n log n 
    max = times[-1] * n 
    l = 0
    r = max
    answer = r
    
    while r - l >= 0:
        mid = (r - l)//2 + l
        # print(l, r, mid)
        result = test(mid,n, times)
        if result:
            # print("오 가능하다!")
            if answer > mid:
                answer = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return answer