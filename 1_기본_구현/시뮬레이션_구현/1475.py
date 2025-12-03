n_str = input()
count = [0] * 10

for n in n_str:
    n = int(n)

    if n in [6, 9]:
        count[6] += 1  # 6, 9 혼용
    else:
        count[n] += 1

count[6] = (count[6] + 1) // 2  # /2 후 반올림
print(max(count))