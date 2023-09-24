for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number = int(input("Number: "))
for i in range(0, number):
    print("*", end="")
print()

# d.
lines = int(input("Lines: "))
for i in range(1, lines + 1):
    print("*" * i)
print()
