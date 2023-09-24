MINIMUM_LENGTH = 8
user_password = input("Password: ")
while len(user_password) < MINIMUM_LENGTH:
    print("Password too short")
    user_password = input("Password: ")
for i in range(len(user_password)):
    print("*", end='')
