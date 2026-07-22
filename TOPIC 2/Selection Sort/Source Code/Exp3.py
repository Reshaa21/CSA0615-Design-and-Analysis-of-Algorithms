books = [305, 102, 250, 118, 199, 400, 101]
moves = 0
for i in range(len(books) - 1):
    min_index = i

    for j in range(i + 1, len(books)):
        if books[j] < books[min_index]:
            min_index = j

    if min_index != i:
        books[i], books[min_index] = books[min_index], books[i]
        moves += 1
print("Sorted Book IDs:", books)
print("Physical Moves:", moves)