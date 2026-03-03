# def solution(citations):
#     answer = 0
#     citations.sort()
#     if len(citations) == 1:
#         return 1
#     for i in range(len(citations)):
#         if len(citations) - i <= citations[i]:
#             # print("멈추기! 이 중 큰 건", citations[i-1], len(citations) - i, max(citations[i-1], len(citations) - i))
#             return len(citations) - i

def solution(citations):
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        h = n - i
        if c >= h:
            return h
    return 0