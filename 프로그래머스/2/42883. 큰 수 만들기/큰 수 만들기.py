# def solution(number, k):
#     answer = ''
#     stack = []
#     for num in number:
#         while stack and stack[-1] < num and k > 0:
#             stack.pop()
#             k -= 1
#         stack.append(num)
#     stack = "".join(stack)
#     return stack

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    # print(len(stack), len(number) - k
    while len(stack) > len(number) - k:
        stack.pop()
    stack = "".join(stack)
    return stack