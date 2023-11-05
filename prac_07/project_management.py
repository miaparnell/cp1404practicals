"""
Time estimate: 2 hours
Actual time:
"""


from project import Project

MENU = "(L)oad\n(S)ave\n(D)isplay\n(F)ilter\n(A)\n(U)pdate"

def main():
    in_filename = 'projects.txt'
    projects = load_data(in_filename)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            in_filename = input("Filename: ")
            projects = load_data(in_filename)
        elif choice == "S":
            out_filename = input("Filename: ")
            save_projects(out_filename, projects)
        elif choice == "D":

        elif choice == "F":

        elif choice == "A":

        elif choice == "U":

        else:
            print("Invalid choice")
        choice = input("Choice: ").upper()
    out_filename = 'projects.txt'
    save_projects(projects)


def load_data(in_filename):
    """Load data from projects.txt"""
    projects = []
    in_file = open(in_filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('    ')
        project = Project(parts[0], parts[1], float(parts[2]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects

def save_projects(out_filename, projects):
    with open(out_filename, 'w', newline="") as out_file:
        for project in projects:
            out_file.write('    '.join(project) + '\n')

def display_projects():

