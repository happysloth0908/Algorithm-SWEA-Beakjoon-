def solution(citations):
    answer = 0
    citations.sort()
    if len(citations) == 1 and citations[0] == 1:
        return 1
    for i in range(len(citations)):
        if len(citations) - i < citations[i]:
            # print("아 숫자는", citations[i], "인데 이것보다 큰건 ", len(citations) - i, "밖에 없음")
            if answer < len(citations) - i: 
                answer = len(citations) - i
            break
        else: answer = citations[i]
    return answer