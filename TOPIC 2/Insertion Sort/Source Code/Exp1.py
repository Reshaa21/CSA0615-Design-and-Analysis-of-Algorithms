leaderboard = [980, 875, 760, 690, 500]
new_score = 820
leaderboard.append(new_score)

for i in range(1, len(leaderboard)):
    key = leaderboard[i]
    j = i - 1

    while j >= 0 and leaderboard[j] < key:
        leaderboard[j + 1] = leaderboard[j]
        j -= 1

    leaderboard[j + 1] = key
print("Updated Leaderboard:")
print(leaderboard)