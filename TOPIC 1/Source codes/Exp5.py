
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)
print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)
result = []
for i in range(rows):
    result.append([0] * cols)
for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            result[i][j] += A[i][k] * B[k][j]

print("Result of Matrix Multiplication:")
for row in result:
    print(row)