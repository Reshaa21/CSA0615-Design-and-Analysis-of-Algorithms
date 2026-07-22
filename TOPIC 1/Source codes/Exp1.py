# Get input from user
arr = list(map(int, input("Enter the elements separated by space: ").split()))

#Create variable "key" to search
key = int(input("Enter the key to search: "))
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Key found at index", i)
        found = True
        break

if found == False:
    print("Key not found")
