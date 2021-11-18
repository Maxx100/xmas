# A --------------------------
# B --------------------------
n, m = tuple(input().split())
m, n = int(m), int(n)

k = n
k_dop = -1
while True:
    star_k_dop = k
    k_dop = k
    if k_dop % (m - 1) >= 1:
        k_dop = k_dop + k_dop // (m - 1)
    else:
        k_dop = k_dop + k_dop // (m - 1) - 1

    if k_dop > n:
        k -= 1
    elif k_dop == n:
        break
    elif k_dop < n:
        k = k + 1
        break
print(k)

# C --------------------------
# D --------------------------
# E --------------------------
