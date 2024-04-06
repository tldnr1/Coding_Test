n = int(input())

stud_info = []
for i in range(n):
    stud_input = input().split()
    stud_info.append((stud_input[0], int(stud_input[1])))

stud_info.sort(key=lambda x: x[1])

for info in stud_info:
    print(info[0], end=' ')
