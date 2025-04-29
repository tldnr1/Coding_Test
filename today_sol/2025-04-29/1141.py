n = int(input())
a = []

for _ in range(n):
    a.append(input().rstrip())

a.sort(key=len)
res = 0

for i in range(n):
    f = False
    for j in range(i + 1, n):
        if a[i] == a[j][0:len(a[i])]:
            f = True
            break

    if not f:
        res += 1

print(res)
