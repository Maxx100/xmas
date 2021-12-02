n, k = [int(i) for i in input().split()]
for _ in range(n):
    arr = [int(i) for i in input().split()]
    arr = sorted(arr)
    summ = sum(arr[0])
    flag = True
    for i in arr[1:]:
        if i >= summ:
            summ += i
        else:
            flag = False
    if flag:
        print('yes')
    else:
        print('no')