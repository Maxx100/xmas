def get_line(arr4):
    arr4 = sorted(arr4, reverse=True)
    arr4 = [str(i) for i in arr4]
    return ''.join(arr4)


n = int(input())
data_n = n
arr = []
arr1, arr2 = [], []

d2 = {
    64: [2, 4, 8],
    32: [4, 8],
    16: [2, 8],
    8: [2, 4],
    4: [4],
    2: [2]
}

d3 = {
    27: [3, 9],
    9: [9],
    3: [3],
}

mnoj_d = {
    2: 0,
    3: 0,
    5: 0,
    7: 0
}

if n == 0:
    print(9876543210)
else:

    if n % 5 == 0:
        mnoj_d[5] = mnoj_d[7] + 1
        arr.append(5)
        n /= 5
    if n % 7 == 0:
        mnoj_d[7] = mnoj_d[7] + 1
        arr.append(7)
        n /= 7

    while n % 2 == 0:
        mnoj_d[2] = mnoj_d[2] + 1
        n /= 2

    while n % 3 == 0:
        mnoj_d[3] = mnoj_d[3] + 1
        n /= 3

    f1 = False
    f2 = False

    # Если не брать 6
    arr1 = arr[:]
    for key in d2:
        if 2 ** mnoj_d[2] == key:
            arr1 = arr1 + d2[key]
            break

    for key in d3:
        if 3 ** mnoj_d[3] == key:
            arr1 = arr1 + d3[key]
            break

    check = 1
    for i in arr1:
        check *= i
    if check == data_n:
        f1 = True

    # Если брать 6
    if data_n % 6 == 0:
        mnoj_d[2] = mnoj_d[2] - 1
        mnoj_d[3] = mnoj_d[3] - 1

        arr2 = arr[:]
        arr2.append(6)

        for key in d2:
            if 2 ** mnoj_d[2] == key:
                arr2 = arr2 + d2[key]
                break

        for key in d3:
            if 3 ** mnoj_d[3] == key:
                arr2 = arr2 + d3[key]
                break

        check = 1
        for i in arr2:
            check *= i
        if check == data_n:
            f2 = True

    if f1 == False and f2 == False:
        print(-1)

    elif f1 and f2:
        arr1.append(1)
        arr2.append(1)
        line1 = int(get_line(arr1))
        line2 = int(get_line(arr2))
        print(max(line1, line2))

    elif f1:
        arr1.append(1)
        line1 = get_line(arr1)
        print(line1)

    elif f2:
        arr2.append(1)
        line2 = get_line(arr2)
        print(line2)
