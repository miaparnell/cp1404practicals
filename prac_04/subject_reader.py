"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject = input("What subject code: ")
    print(f"{subject_to_data[subject][0]} teaches {subject}")
    # display_subjects(subjects)



def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject.append(parts)
    input_file.close()
    return subject

def convert_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data

def display_subjects(subjects):
    """Display the subject name, teacher, and number of students."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()