def find_second_lowest_grade_students(students):
    # Sort the students by grade
    sorted_students = sorted(students, key=lambda x: x[1])
    
    # Find the second lowest grade
    grades = [student[1] for student in sorted_students]
    unique_grades = sorted(set(grades))
    if len(unique_grades) < 2:
        return []  # Not enough unique grades
    second_lowest_grade = unique_grades[1]

    # Find students with the second lowest grade
    second_lowest_students = [student[0] for student in sorted_students if student[1] == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    return second_lowest_students

def main():
    # Read input
    N = int(input())
    students = []
    for _ in range(N):
        name = input()
        grade = float(input())
        students.append([name, grade])
    
    # Find and print students with second lowest grade
    result = find_second_lowest_grade_students(students)
    for name in result:
        print(name)

if __name__ == "__main__":
    main()