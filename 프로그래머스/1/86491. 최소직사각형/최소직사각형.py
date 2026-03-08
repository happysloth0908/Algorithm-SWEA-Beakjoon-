def solution(sizes):
    mins = []
    maxs = []
    for card in sizes:
        mins.append(min(card))
        maxs.append(max(card))
        
    min_max = max(mins)
    max_max = max(maxs)
    
    return min_max * max_max
