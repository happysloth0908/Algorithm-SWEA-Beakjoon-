
n = int(input())

for _ in range(n):
    is_reverse = False

    command = input()
    length = input()
    arr = eval(input())

    for i in range(len(command)):
        # print(f"명령 {i}번째: {command[i]}")

        if command[i] == 'D':
            if len(arr) == 0:
                arr = 'error'
                is_reverse = False
                break
            if not is_reverse:
                arr.pop(0)
            else:
                arr.pop(len(arr)-1)


        elif command[i] == 'R':
             is_reverse = not is_reverse

    if arr == 'error':
        print('error')
    elif is_reverse:
        arr = arr[::-1]
        print('[' + ','.join(map(str, arr)) + ']')
    else:
        print('[' + ','.join(map(str, arr)) + ']')

