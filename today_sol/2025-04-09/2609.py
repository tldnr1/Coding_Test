from math import gcd
a, b = map(int, input().split())

g = gcd(a, b)

print(g)
print(a * b // g)
