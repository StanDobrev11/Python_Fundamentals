class Class:
    __student__count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.av_grade = 0

    def add_student(self, name, grade):
        self.students.append(name)
        if len(self.students) > Class.__student__count:
            self.students.pop()
        self.grades.append(grade)
        if len(self.grades) > Class.__student__count:
            self.grades.pop()

    def get_average_grade(self):
        self.av_grade = f"{sum(self.grades) / len(self.grades) :.2f}"
        return self.av_grade

    def __repr__(self):
        self.av_grade = f"{sum(self.grades) / len(self.grades) :.2f}"
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.av_grade}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
