cards = [7, 2, 9, 4, 1]
hand = []
for card in cards:
    hand.append(card)

    # Insertion Sort
    for i in range(1, len(hand)):
        key = hand[i]
        j = i - 1

        while j >= 0 and hand[j] > key:
            hand[j + 1] = hand[j]
            j -= 1

        hand[j + 1] = key

print("Sorted Hand:")
print(hand)