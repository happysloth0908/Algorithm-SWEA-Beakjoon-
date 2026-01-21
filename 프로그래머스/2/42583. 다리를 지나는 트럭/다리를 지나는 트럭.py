# 다리에 있는 트럭 무게를 재기 위해 매번 sum(deque) 를 써서 시간초과가 남!!

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck_weights_deque = deque(truck_weights)
    # print(truck_weights_deque)
    # print(truck_weights_deque[0])
    # print(sum(truck_weights))
    
    total_weight = sum(truck_weights)
    pass_weight = 0
    time = 0
    weight_on_bridge = 0
    
    while pass_weight < total_weight: 
        time += 1
        off_bridge = bridge.pop()
        pass_weight += off_bridge #오른쪽에서 빼내고 
        weight_on_bridge -= off_bridge
        if truck_weights_deque and weight_on_bridge + truck_weights_deque[0] <= weight:
            on_bridge = truck_weights_deque.popleft()
            bridge.appendleft(on_bridge)
            weight_on_bridge += on_bridge
             
                
        else: 
            bridge.appendleft(0)
            
        
    return time