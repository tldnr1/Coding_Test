import re
from collections import Counter

def sol(s):
    reduced = re.sub(r'(.)\1+', r'\1', s)
    counts = Counter(reduced)
    
    if any(count >= 2 for count in counts.values()):
        return 0
    else:
        return 1


count = 0
n = int(input())
for _ in range(n):
    word = input()
    count += sol(word)
print(count)
