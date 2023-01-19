class Student:
    def __init__(self, name, age, grade):
        self.grade = grade
        self.age = age
        self.name = name

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.max_students = max_students
        self.name = name
        self.students = []

    def add_student(self, student):
        if self.students < self.max_students:
            self.students.append(student)


student1 = Student("isuru", 20, 80)
student2 = Student("man", 25, 85)
student3 = Student("ann", 28, 90)

course = Course("web Devolopment", 2)
course.add_student(student1)
course.add_student(student2)

