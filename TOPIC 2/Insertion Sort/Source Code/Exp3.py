prices = [102.5, 98.3, 105.1, 100.0, 97.8]
sorted_prices = []
for price in prices:
    sorted_prices.append(price)

    # Insertion Sort
    for i in range(1, len(sorted_prices)):
        key = sorted_prices[i]
        j = i - 1

        while j >= 0 and sorted_prices[j] > key:
            sorted_prices[j + 1] = sorted_prices[j]
            j -= 1

        sorted_prices[j + 1] = key
print("Sorted Prices:")
print(sorted_prices)