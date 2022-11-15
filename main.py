from gpa_calculations    import Semester, CgpaCalculator

no_of_semesters = int(input("How many semesters: "))
semester_list = []
for num in range(no_of_semesters):
    semester = Semester(int(input(f"How many courses in semester {num+1}: ")))
    print(f"Enter appropriate values for semester {num+1}")
    semester.create_course_dictionary()
    print(semester.course_dict)
    semester_list.append(semester)
cgpa_calculator = CgpaCalculator(semester_list)
print("\n\n")
cgpa_calculator.print_gpas()
user_cgpa = cgpa_calculator.calculate_cgpa()
print(f"\n\nCGPA: {user_cgpa}")
if user_cgpa >= 4.5:
    print("Class: First")
elif user_cgpa >= 3.5:
    print("Class: Second Class Upper")
elif user_cgpa >= 2.5:
    print("Class: Second Class Lower")
elif user_cgpa >= 1.5:
    print("Class: Third Class")
else:
    print("Failure")

