"""
Emails
Estimated: 25 minutes
Actual: 30 minutes
"""

email_to_name = {}
email = input("Enter email: ")
while email != "":
    first_part_of_email = email.split('@')[0]
    parts_of_email = first_part_of_email.split('.')
    name = " ".join(parts_of_email).title()
    name_confirmation = input(f"Is {name} your name? (Y/n) ").upper()
    if name_confirmation != "Y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Enter email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
