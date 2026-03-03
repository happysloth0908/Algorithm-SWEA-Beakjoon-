def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if len(citations) - i <= citations[i]:
            return len(citations) - i
    return 0

# def solution(citations):
#     citations.sort()
#     n = len(citations)
#     for i, c in enumerate(citations):
#         h = n - i
#         if c >= h:
#             return h
#     return 0