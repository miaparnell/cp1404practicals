# question 1:
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# question 2:
in_file = open("name.txt", 'r')
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# question 3
in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
total = first_number + second_number
print(total)
in_file.close()

# question 4
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()

