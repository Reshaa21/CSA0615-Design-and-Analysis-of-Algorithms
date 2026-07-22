prices = [499, 129, 899, 45, 275, 60, 310, 150]
for i in range(len(prices) - 1):
    min_index = i

    for j in range(i + 1, len(prices)):
        if prices[j] < prices[min_index]:
            min_index = j

    prices[i], prices[min_index] = prices[min_index], prices[i]
print("Sorted Prices:")
print(prices)