def solution(numbers, target):
    sum = 0
    def dfs(n, i):
        nonlocal sum
        i+=1
        if i == len(numbers):
            if n == target:
                sum +=1
            return
        dfs(n + numbers[i], i)
        dfs(n - numbers[i], i)
    
    dfs(0, -1)
    
    return sum