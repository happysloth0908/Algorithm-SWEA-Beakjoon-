from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    print(list(p - c))
    answer = list(p - c)[0]
    return answer