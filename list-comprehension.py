x, y, z, n = map(int, input().split())

# Generate all possible coordinates (i, j, k) using list comprehensions
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

print(coordinates)


# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i + j + k !=n:
#                 print(i,j,k)