scores = [72, 88, 65, 90, 77, 95, 60, 83, 91, 68]
k = 5

for i in range(k):
    max_index = i

    for j in range(i + 1, len(scores)):
        if scores[j] > scores[max_index]:
            max_index = j

    scores[i], scores[max_index] = scores[max_index], scores[i]
print("Top", k, "Scores:")
print(scores[:k])