numbers = [5, 1, 4, 2, 8]
print("Original:", numbers)
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("After Pass", i + 1, ":", numbers)