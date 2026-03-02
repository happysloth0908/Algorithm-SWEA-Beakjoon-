def solution(people, limit):
    people.sort()
    answer = 0
    i = len(people) -1 
    j = 0
    boat = 0
    while i >= 0 and i >= j:
        if i == 0:
            boat += 1
            break
        
        if limit - people[i] >= people[j] :
            j += 1
        boat += 1
        
        i -= 1
        
    return boat