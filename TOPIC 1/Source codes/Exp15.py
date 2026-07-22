import math
n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x, y = map(int, input("Enter x and y coordinates: ").split())
    points.append((x, y))
min_distance = float("inf")
point1 = ()
point2 = ()

for i in range(n):
    for j in range(i + 1, n):
        distance = math.sqrt((points[i][0] - points[j][0])**2 +
                             (points[i][1] - points[j][1])**2)

        if distance < min_distance:
            min_distance = distance
            point1 = points[i]
            point2 = points[j]
print("Closest pair:", point1, "and", point2)
print("Distance =", min_distance)