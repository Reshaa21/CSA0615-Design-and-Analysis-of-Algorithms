arr = list(map(int, input("Enter the elements separated by space: ").split()))
max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)
print("Maximum Subarray Sum:", max_sum)