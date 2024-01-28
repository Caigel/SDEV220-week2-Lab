
#Author, Caige laurenti
#File name: SDEV220-02-Lab
#description: lets user enter students names and GPA's until ZZZ is entered. after ZZZ is entered it tells you weather the gpa was good 
#enough to make the deans list or the honor roll

# Gets the name and GPA of students
def get_input():
    name = input("Enter name (or 'ZZZ' to quit): ")
    if name.upper() == 'ZZZ':
        return None, None
    gpa = float(input("Enter GPA: "))
    return name, gpa


# Checks the gpa with the set standards for honor roll and deans list
def check_gpa(students):
    for student in students:
        if student['gpa'] >= 3.5:
            print(f"{student['name']} has made the dean's list!")
        elif student['gpa'] >= 3.25:
            print(f"{student['name']} has made the honor roll!")
        elif student['gpa'] < 3.25:
            print(f"{student['name']} has not made the honor roll or the deans list")


# runs the program
def main():
    students = []
    while True:
        name, gpa = get_input()
        if name is None:
            break
        student = {"name": name, "gpa": gpa}
        students.append(student)
    check_gpa(students)

if __name__ == "__main__":
    main()