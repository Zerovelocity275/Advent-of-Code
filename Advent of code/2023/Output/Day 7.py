with open('Input/Day 7.txt', 'r') as file:
   lis = file.read().split('\n')

hands = [[hand.split(' ')[0], int(hand.split(' ')[1])] for hand in lis]
hands2 = [[hand.split(' ')[0], int(hand.split(' ')[1])] for hand in lis]
cardstrength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
totalbet, totalbet2 = 0, 0

def handtype(hand, part):
    if part == 2:
        joker = hand.find('J')
        if joker > -1:
            return max([handtype(hand[0:joker] + card + hand[joker + 1:5], 2) for card in cardstrength[:12]])
    cards = {card:hand.count(card) for card in hand}
    if len(cards) == 1:
        return 6
    if len(cards) == 2:
        return 5 if 4 in cards.values() else 4
    if len(cards) == 3:
        return 3 if 3 in cards.values() else 2
    if len(cards) == 4:
        return 1
    return 0

def sort(x):
    handstrength = []
    for  card in range(len(x[0])):
        handstrength.append(len(cardstrength)-cardstrength.index(x[0][card]))
    return x[2], handstrength

for i in range(len(hands)):
    hands[i].append(handtype(hands[i][0], 1))

cardstrength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

for i in range(len(hands2)):
    hands2[i].append(handtype(hands2[i][0], 2))

hands.sort(key=sort)
hands2.sort(key=sort)

for bet in range(len(hands)):
    totalbet += hands[bet][1]*(bet+1)
    totalbet2 += hands2[bet][1]*(bet+1)

print(f'Answer for part 1 is: {totalbet}\nAnswer for part 2 is: {totalbet2}')    