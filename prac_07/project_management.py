"""
Time estimate: 2 hours
Actual time: 2 hours 15 minutes
"""


from project import Project
import datetime

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"


def main():
    in_filename = 'projects.txt'
    projects = load_data(in_filename)
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            in_filename = input("Filename: ")
            projects = load_data(in_filename)
        elif choice == "S":
            out_filename = input("Filename: ")
            save_projects(out_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def display_projects(projects):
    """Display the projects separated by their completion status."""
    for i, project in enumerate(projects, 1):
        print("Completed projects: ")
        if project.is_complete():
            print(project)
        print("Incomplete projects: ")
        if project.is_not_complete():
            print(project)


def filter_projects(projects):
    """Filter the projects by date."""
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project!")
    name = input("Name: ")
    start_date = input("Start date (d/m/yyyy):")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Completion percentage: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update the percentage or priority level of a project."""
    project_number = 0
    for project in projects:
        print(project_number, project)
        project_number += 1
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New percentage: "))
    projects[project_choice][4] = new_percentage
    new_priority = int(input("New priority: "))
    projects[project_choice][2] = new_priority


def save_projects(out_filename, projects):
    """Save the projects to a file."""
    with open(out_filename, 'w', newline="") as out_file:
        for project in projects:
            out_file.write('    '.join(project) + '\n')


main()
