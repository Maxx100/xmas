a = [int(i) for i in input().split()]

poluch = a[0]
hod = a[1]

if poluch % hod != 0:
    print(poluch - poluch // hod)
else:
    print(poluch - poluch // hod + 1)
