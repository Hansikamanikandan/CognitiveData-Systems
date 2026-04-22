r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

A = []
print("Enter first matrix:")
for i in range(r1):
    A.append(list(map(int, input().split())))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

B = []
print("Enter second matrix:")
for i in range(r2):
    B.append(list(map(int, input().split())))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    result = [[0]*c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result Matrix:")
    for row in result:
        print(row)
