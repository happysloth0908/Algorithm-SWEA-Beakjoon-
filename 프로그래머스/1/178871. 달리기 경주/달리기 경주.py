from collections import defaultdict
def solution(players, callings):
    answer = []
    name_st = defaultdict(int)
    st_name = defaultdict(str)
    
    
    for i in range(len(players)):
        name_st[players[i]] += i
        st_name[i] += players[i]
        
    for call in callings:
        #이름:등수 dict 처리
        name_st[call] -= 1
        name_st[st_name[name_st[call]]] += 1
        
        #추월한 등수 (좋은 등수)
        h = name_st[call]
        
        #등수:이름 dict 처리
        #높은 등수에 추월 선수 이름 넣기
        loser_name = st_name[h]
        winner_name = st_name[h + 1] 
        st_name[h] = winner_name
        st_name[h + 1] = loser_name
        
        #낮은 등수에 추월 당한 선수 이름 넣기
        
        
        # match[match[call]] += 1
        # 아아..?! 이런 식으로 value 로 key 를 찾아야 할 때는 dict 두개 써야 한다!
        
        
        
    # for name in st_name:
    #     print(name)
    #     # answer.append(name.values())
    # print(st_name)
    answer = list(st_name.values())
    
    return answer