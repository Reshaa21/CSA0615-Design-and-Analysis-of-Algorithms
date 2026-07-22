n = int(input("Enter the number of terms: "))
print("Fibonacci Series using Iterative Method:")
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print("Fibonacci Series using Recursive Method:")
for i in range(n):
    print(fibonacci(i), end=" ")