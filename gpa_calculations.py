GRADES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "F": 0
}


class Semester:

    def __init__(self, number_of_courses: int):
        self.courses = number_of_courses
        self.course_dict = {}

    def create_course_dictionary(self):
        course_dict = {}
        for values in range(self.courses):
            course_code = input("Enter Course Code: ")
            try:
                units = int(input(f"How many units is {course_code}: "))
            except ValueError:
                print("Enter a number")
                units = int(input(f"How many units is {course_code}: "))
            course_data = {
                course_code: [units, input(f"What was your grade in {course_code} (A, B, C, D or F): ").upper()]
            }
            course_dict.update(course_data)
            self.course_dict = course_dict


def calculate_gpa(course_dict: dict):
    total_grade_points = 0
    accumulated_grade_points = 0
    for value in course_dict.values():
        total_grade_points += value[0] * 5
        accumulated_grade_points += GRADES[value[1]] * value[0]
    gpa = 5 * (accumulated_grade_points / total_grade_points)
    gpa = round(gpa, 2)
    return gpa


class CgpaCalculator:
    def __init__(self, semesters_list: list):
        self.semesters = semesters_list
        self.gpa_list = []

    def print_gpas(self):
        gpa_list = []
        for semester in self.semesters:
            gpa_list.append(calculate_gpa(semester.course_dict))
        self.gpa_list = gpa_list
        gpa_list_length = len(self.gpa_list)
        for num in range(gpa_list_length):
            print(f"Semester {num + 1} GPA: {self.gpa_list[num]}")

    def calculate_cgpa(self):
        total_gp = 0
        attained_gp = 0
        for semester in self.semesters:
            for value in semester.course_dict.values():
                total_gp += value[0] * 5
                attained_gp += GRADES[value[1]] * value[0]
        cgpa = round(5 * (attained_gp / total_gp), 2)
        return cgpa
