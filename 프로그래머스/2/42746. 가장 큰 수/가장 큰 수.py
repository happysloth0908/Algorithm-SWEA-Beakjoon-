from functools import cmp_to_key
def solution(numbers):
    answer = ''
    string_num = list(map(str, numbers))

    string_num.sort(key=cmp_to_key(lambda x,y : -1 if x+y > y+x else 1) )

    answer = "".join(string_num)
    answer = int(answer)
    answer = str(answer)
    return answer