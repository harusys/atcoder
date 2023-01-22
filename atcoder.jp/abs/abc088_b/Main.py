N = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)
Alice = cards[0::2]
Bob = cards[1::2]

print(sum(Alice) - sum(Bob))