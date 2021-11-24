a = int(input())
b = int(input())
ans = [a // 3, a % 3, b // 3]
a %= 3
b %= 3
if a != b:
    print(-1)
else:
    print(*ans)
