playlist = [
    ("Intro", 120),
    ("Chill Beat", 210),
    ("Long Jam", 340)
]
new_song = ("Quick Track", 180)
playlist.append(new_song)

for i in range(1, len(playlist)):
    key = playlist[i]
    j = i - 1

    while j >= 0 and playlist[j][1] > key[1]:
        playlist[j + 1] = playlist[j]
        j -= 1

    playlist[j + 1] = key
print("Updated Playlist:")
for song in playlist:
    print(song)