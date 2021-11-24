n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
s = list(reversed(list(input())))

ll, rr = [a[i] for i in range(0, n, 2)], [a[i] for i in range(1, n, 2)]
if s[0] == "R":
    ll, rr = rr, ll


ans = []
for i in range(n):
    if s[i] == "L":
        if s[i - 1] == "L":
            ans.append([ll[-1], "L"])
            ll.pop(-1)
        else:
            ans.append([ll[0], "L"])
            ll.pop(0)
    else:
        if s[i - 1] == "L":
            ans.append([rr[0], "R"])
            rr.pop(0)
        else:
            ans.append([rr[-1], "R"])
            rr.pop(-1)

if s[0] == "L":
    for i in ans:
        print(*i)
else:
    for i in ans:
        if i[1] == "L":
            print(i[0], "R")
        else:
            print(i[0], "L")
