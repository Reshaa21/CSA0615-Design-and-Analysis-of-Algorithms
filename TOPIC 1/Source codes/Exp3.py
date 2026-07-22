n = int(input("Enter a number: "))

fact1 = 1
for i in range(1, n + 1):
    fact1 = fact1 * i

print("Factorial using Iterative Method:", fact1)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

fact2 = factorial(n)
print("Factorial using Recursive Method:", fact2)