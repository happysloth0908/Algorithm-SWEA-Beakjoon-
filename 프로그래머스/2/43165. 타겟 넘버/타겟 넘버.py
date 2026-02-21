def solution(numbers, target):
    sum = 0
    def dfs(n, i):
        nonlocal sum
        if i == len(numbers):
            if n == target:
                sum +=1
            return
        dfs(n + numbers[i], i + 1)
        dfs(n - numbers[i], i + 1)
    
    dfs(0, 0)
    
    return sum