from functools import cmp_to_key
def solution(numbers):
    
    def compare(a,b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        else: return 1
    
    numbers.sort(key=cmp_to_key(compare))
    numbers = list(map(str, numbers))
    
    return str(int("".join(numbers)))