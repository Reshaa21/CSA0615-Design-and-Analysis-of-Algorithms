roll_numbers = [101, 102, 104, 103, 105, 107, 106, 108]
passes = 0
for i in range(len(roll_numbers) - 1):
    swapped = False
    passes += 1

    for j in range(len(roll_numbers) - 1 - i):
        if roll_numbers[j] > roll_numbers[j + 1]:
            roll_numbers[j], roll_numbers[j + 1] = roll_numbers[j + 1], roll_numbers[j]
            swapped = True

    if not swapped:
        break
print("Sorted Roll Numbers:", roll_numbers)
print("Passes:", passes)