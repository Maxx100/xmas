for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % 2 == 1:
        print("NO")
    else:
        temp1 = 0
        temp2 = 0
        for i in a:
            if i == 1:
                temp1 += 1
            else:
                temp2 += 1
        temp2 %= 2
        if temp2 == 1:
            if temp1 < 2:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
