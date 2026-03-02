def solution(people, limit):
    people.sort()
    answer = 0
    i = len(people) -1 
    j = 0
    boat = 0
    escaped = set()
    while i >= 0 and i >= j:
        # print(i,j)
        if i == 0 and i not in escaped:
            boat += 1
            # print("0번 손님 태우고 이제 빠집니다")
            break
        
        if i not in escaped: 
            if limit - people[i] >= people[j] and j not in escaped:
                escaped.add(j)
                escaped.add(i)
                j += 1
                # print(i, j , "태운 배 하나 감")
            else:
                escaped.add(i)
                # print(limit - people[i] >= people[j])
                # print(i,"태운 배 하나 감")
            boat += 1
        
        i -= 1
        
    return boat