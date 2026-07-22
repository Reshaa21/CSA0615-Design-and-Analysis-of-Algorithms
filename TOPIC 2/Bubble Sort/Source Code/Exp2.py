queue = ["car", "car", "bus", "ambulance"]
priority = {
    "ambulance": 1,
    "bus": 2,
    "car": 3
}
for i in range(len(queue) - 1):
    for j in range(len(queue) - 1 - i):
        if priority[queue[j]] > priority[queue[j + 1]]:
            queue[j], queue[j + 1] = queue[j + 1], queue[j]
print("Priority Queue:")
print(queue)