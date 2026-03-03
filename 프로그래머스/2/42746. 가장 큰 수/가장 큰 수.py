from functools import cmp_to_key
def solution(numbers):
    answer = ''
    def compare(a,b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        else: return 1
    
    numbers.sort(key=cmp_to_key(compare))
    # print(numbers)
    stringy = ""
    for number in numbers:
        stringy += str(number)
    ans = int(stringy)
    
    return str(ans)