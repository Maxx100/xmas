a = int(input())
b = int(input())
res = [0, 0, 0]
res[0] = a // 3
a = a % 3
res[1] = b // 3
b = b % 3
if a != b:
    print(-1)
else:
    res[2] = a
    print(res[0], res[2], res[1])
