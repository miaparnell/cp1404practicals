NAME_TO_CODE = {"Brilliant Rose": "ff55a3", "Baby Blue": "89cff0", "Bright Lilac": "d891ef", "Corn": "fbec5d",
                "Cosmic Latte": "fff8e7", "Cotton Candy": "ffbcd9", "DarkSeaGreen1": "c1ffc1", "Deep Peach": "ffcba4",
                "Ghost White": "f8f8ff", "Golden Yellow": "ffdf00"}

hex_name = input("Enter hex colour name: ").title()
while hex_name != "":
    try:
        print(f"The code for {hex_name} is #{NAME_TO_CODE[hex_name]}")
    except KeyError:
        print("Invalid hex name")
    hex_name = input("Enter hex colour name: ").title()

