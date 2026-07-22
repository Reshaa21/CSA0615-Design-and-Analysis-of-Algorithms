def iterative_power(x, n):
    result = 1
    for i in range(n):
        result = result * x
    return result
def recursive_power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = recursive_power(x, n // 2)
        return half * half
    else:
        return x * recursive_power(x, n - 1)

x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
print("Iterative Power:", iterative_power(x, n))
print("Recursive Fast Power:", recursive_power(x, n))