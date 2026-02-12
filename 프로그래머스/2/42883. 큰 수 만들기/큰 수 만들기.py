def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    # while len(stack) > len(number) - k:
    #     stack.pop() 와 while 문 안 쓰고 슬라이싱으로 할 수 있음. 
    if len(stack) > len(number) - k:
        stack = stack[:-k]
    stack = "".join(stack)
    return stack