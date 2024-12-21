n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

min_card = []
for card in cards:
    min_card.append(min(card))

print(max(min_card))
