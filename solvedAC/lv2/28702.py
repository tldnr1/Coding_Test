import sys

input = sys.stdin.readline

# main
words = []
for _ in range(3):
    words.append(input().rstrip())

t = 0
for i in range(3):
    if words[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        t = i
        break

target = int(words[t]) + 3 - t
if target % 15 == 0:
    print("FizzBuzz")
elif target % 3 == 0:
    print("Fizz")
elif target % 5 == 0:
    print("Buzz")
else:
    print(target)