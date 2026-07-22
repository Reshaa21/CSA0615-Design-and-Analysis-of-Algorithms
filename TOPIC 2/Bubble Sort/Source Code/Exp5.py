hand = [2, 4, 6, 8, 9, 11, 13]
hand.append(7)
passes = 0
for i in range(len(hand) - 1):
    swapped = False
    passes += 1

    for j in range(len(hand) - 1 - i):
        if hand[j] > hand[j + 1]:
            hand[j], hand[j + 1] = hand[j + 1], hand[j]
            swapped = True

    if not swapped:
        break

print("Sorted Hand:", hand)
print("Passes:", passes)