n = int(input())
arr = [int(i) for i in input().split()]

ans1 = sum(arr) % n

k = sum(arr) // n
ans2 = 0
for i in arr:
    if i > k:
        ans2 += abs(k - i)

print(ans1, ans2 - ans1)
