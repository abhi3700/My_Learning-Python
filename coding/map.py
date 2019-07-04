# Example-1
items = [1, 2, 3, 4, 5]

# M-1
squared = []
for i in items:
    squared.append(i**2)
print(squared)

# M-2
squared2 = list(map(lambda x: x**2, items))
print(squared2)
# ----------------------------------------------------------
# Example-2
s = 'geeks'
# M-1
U = []
for c in s:
    U.append(c.upper())
print(U)

# M-2
U = list(map(str.upper, s))
print(U)