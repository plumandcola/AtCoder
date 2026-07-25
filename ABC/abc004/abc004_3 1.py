#30点解法
cards = list(range(1, 7))

N = int(input())
for i in range(N):
    cards[i%5], cards[i%5 + 1] = cards[i%5 + 1], cards[i%5]

print(*cards, sep="")