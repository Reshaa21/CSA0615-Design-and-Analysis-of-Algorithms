log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0]
shifts = 0
for i in range(1, len(log)):
    key = log[i]
    j = i - 1

    while j >= 0 and log[j] > key:
        log[j + 1] = log[j]
        j -= 1
        shifts += 1

    log[j + 1] = key
print("Sorted Log:")
print(log)
print("Total Shifts:", shifts)