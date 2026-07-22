numbers = [23.5, 19.2, 25.1, 18.8, 21.4]
swaps = 0
for i in range(len(numbers) - 1):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    if min_index != i:
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        swaps += 1
print("Sorted List:", numbers)
print("Total Swaps:", swaps)