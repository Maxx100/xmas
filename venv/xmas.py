# A --------------------------
# B --------------------------
# C --------------------------
n = int(input())

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
ans = []

for i in a:
    if n % i == 0:
        ans.append(i)
        n //= i
if 8 in ans:
    if 4 not in ans and 2 not in ans:
        ans.remove(8)
        ans.append(4)
        ans.append(2)
if 6 in ans:
    if 3 not in ans and 2 not in ans:
        ans.remove(6)
        ans.append(3)
        ans.append(2)
ans.sort(reverse=True)
if n == 1:
    print("".join(list(map(str, ans))))
else:
    print(-1)
# D --------------------------
# E --------------------------
