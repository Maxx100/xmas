k, r, n = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if i == k:
        ans += r
    elif i > k:
        ans += 2 * r
    else:
        ans += r + i - k
print(ans)
