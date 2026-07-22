alerts = [2, 1, 3, 2, 1, 4, 3, 2, 5, 1]
comparisons = 0
for i in range(len(alerts) - 1):
    swapped = False
    for j in range(len(alerts) - 1 - i):
        comparisons += 1

        if alerts[j] > alerts[j + 1]:
            alerts[j], alerts[j + 1] = alerts[j + 1], alerts[j]
            swapped = True

    if not swapped:
        break
print("Sorted Alerts:", alerts)
print("Comparisons:", comparisons)