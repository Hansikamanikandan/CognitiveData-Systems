n = int(input("Enter value of n: "))
square_map = {}

for x in range(1, n + 1):
    square_map[x] = x * x

print(square_map)
