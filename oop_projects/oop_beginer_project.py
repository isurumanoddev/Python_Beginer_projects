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
        if len(self.students) < self.max_students:
            self.students.append(student)

    def get_average(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total/len(self.students)


student1 = Student("isuru", 20, 80)
student2 = Student("man", 25, 85)
student3 = Student("ann", 28, 90)

course = Course("web Devolopment", 2)
course.add_student(student1)
course.add_student(student2)


# inheritance

class Pet:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def show(self):
        print(f"I am {self.name} and {self.age} years old")

class Dog(Pet):
    def __init__(self, color, name, age):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("bark")

    def color_(self):
        print(f"Color is {self.color}")

class Cat(Pet):
    def speak(self):
        print("Meow")


dog = Dog("Lazzy",6,"black")
dog.show()
dog.speak()
dog.color_()
cat = Cat("Garfield", 10)
cat.show()
