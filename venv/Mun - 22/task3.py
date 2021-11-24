n = int(input())

a = list(range(9, 0, -1))

if n == 0:
    print(9876543210)
else:
    ans = []
    for i in a:
        if n % i == 0:
            ans.append(i)
            n //= i
    if (6 in ans) and (2 not in ans) and (3 not in ans):
        ans.remove(6)
        ans += [2, 3]
    elif (8 in ans) and (2 not in ans) and (4 not in ans):
        ans.remove(8)
        ans += [2, 4]
    if (9 in ans) and (4 in ans) and (3 not in ans) and (6 not in ans) and (2 not in ans):
        ans.remove(9)
        ans.remove(4)
        ans += [3, 6, 2]

    if n == 1:
        print("".join(map(str, sorted(ans, reverse=True))))
    else:
        print(-1)
