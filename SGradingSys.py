# create an empty list to store collected data
CSC2023_students = []

# creates a base class


class Person:
    def __init__(self, name, national_id):
        self.name = name
        self.National_Id_No = national_id


class Student(Person):
    def __init__(self, name, national_id, student_id, course_1, grade_1, course_2, grade_2, course_3, grade_3, course_4, grade_4, course_5=None, grade_5=0, course_6=None, grade_6=0, course_7=None, grade_7=0):
        super().__init__(name, national_id)
        self.student_id = student_id
        self.course_1 = course_1
        self.grade_1 = grade_1
        self.course_2 = course_2
        self.grade_2 = grade_2
        self.course_3 = course_3
        self.grade_3 = grade_3
        self.course_4 = course_4
        self.grade_4 = grade_4
        self.course_5 = course_5
        self.grade_5 = grade_5
        self.course_6 = course_6
        self.grade_6 = grade_6
        self.course_7 = course_7
        self.grade_7 = grade_7

        CSC2023_students.append(
            {
                "Name": self.name,
                "National ID No": self.National_Id_No,
                "Student ID No": self.student_id,
                self.course_1: self.grade_1,
                self.course_2: self.grade_2,
                self.course_3: self.grade_3,
                self.course_4: self.grade_4,
                self.course_5: self.grade_5,
                self.course_6: self.course_6,
                self.course_7: self.grade_7,
            }
        )

    def calc_average_score(self):
        optional_grade = [self.grade_5, self.grade_6, self.grade_7]
        count = 0

        for each_grade in optional_grade:
            if each_grade != 0:
                count += 1

        av_score = (self.grade_1+self.grade_2+self.grade_3 +
                    self.grade_4+self.grade_5+self.grade_6+self.grade_7)/(4+count)
        performance = None
        if 0 <= av_score <= 40:
            performance = "poor"
        elif 41 <= av_score <= 50:
            performance = "Fair"
        elif 51 <= av_score <= 60:
            performance = "Good"
        elif 61 <= av_score <= 70:
            performance = "Very Good"
        elif 71 <= av_score <= 99:
            performance = "Excellent"
        elif av_score == 100:
            performance = "Cheated"

        print(f"{self.name}'s Average Score is {av_score}")
        print(performance)


class Teacher(Student):

    def __init__(self, teacher_name, teacher_id, name, national_id, student_id, course_1, grade_1, course_2, grade_2, course_3, grade_3, course_4, grade_4, course_5=None, grade_5=0, course_6=None, grade_6=0, course_7=None, grade_7=0):
        super().__init__(name, national_id, student_id, course_1, grade_1, course_2, grade_2, course_3,
                         grade_3, course_4, grade_4, course_5, grade_5, course_6, grade_6, course_7, grade_7)
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id

    def edit_data(self, name, data_to_be_edited, new_value):
        for student in CSC2023_students:
            if student["Name"] == name:
                student[data_to_be_edited] = new_value


teacher_1 = Teacher("Dr.Barnes", "U_Teach102/2025", "Bola", "Nig/23445", "CSC/2024/010",
                    "CSC101", 70, "MTH101", 60, "CHM101", 80, "PHY101", 50, "TPD101", 60)
teacher_1.calc_average_score()
print(CSC2023_students.copy())
