from typing import Type


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade, student):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        divisor = 0
        sum_ball = 0
        for students_ball in self.grades.values():
            sum_ball += sum(students_ball)
            divisor += len(students_ball)
        return format(sum_ball / divisor, '.1f')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses} "
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_lec_grades(self):
        divisor = 0
        sum_ball = 0
        for lec_ball in self.grades.values():
            sum_ball += sum(lec_ball)
            divisor += len(lec_ball)
        return format(sum_ball / divisor, '.1f')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_lec_grades() < other.average_lec_grades()

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_lec_grades()}"
        return text


reviewr1 = Reviewer('Ivan', 'Popov')
reviewr1.courses_attached += ['Python']
reviewr2 = Reviewer('Katerina', 'Queen')
reviewr2.courses_attached += ['Python']
lector1 = Lecturer('Igor', 'Popovuth')
lector2 = Lecturer('Vaka', 'Kusaev')
lector1.courses_attached += ['Git', 'Python']
lector2.courses_attached += ['Python']
student1 = Student('Nikola', 'Pagankin', 'men')
student1.finished_courses += ['Java']
student1.courses_in_progress += ['Python']
student2 = Student('Irina', 'Knyz', 'women')
student2.finished_courses += ['Git']
student2.courses_in_progress += ['Java', 'Python']
student_list = [student1, student2]
lector_list = [lector1, lector2]
student1.rate_lec(lector1, 'Python', 9, student1)
student1.rate_lec(lector1, 'Python', 10, student1)
student1.rate_lec(lector1, 'Python', 9, student1)
student2.rate_lec(lector2, 'Python', 9, student1)
student2.rate_lec(lector2, 'Python', 10, student1)
student2.rate_lec(lector2, 'Python', 8, student1)
reviewr1.rate_hw(student1, 'Python', 9)
reviewr1.rate_hw(student1, 'Python', 8)
reviewr1.rate_hw(student1, 'Python', 9)
reviewr2.rate_hw(student2, 'Python', 9)
reviewr2.rate_hw(student2, 'Python', 9)
reviewr2.rate_hw(student2, 'Python', 10)


def info_average_student(course, student_list):
    grades_list = []
    div = 0
    sum_b = 0
    for grade in student_list:
        if course in grade.grades.keys():
            grades_list.append(grade.grades.get(course))
            for aver_ball in grades_list:
                sum_b += sum(aver_ball)
                div += len(aver_ball)
            return format(sum_b / div, '.1f')


def info_average_lecturer(course, lector_list):
    grades_list = []
    div = 0
    sum_b = 0
    for grade in lector_list:
        if course in grade.grades.keys():
            grades_list.append(grade.grades.get(course))
            for aver_ball in grades_list:
                sum_b += sum(aver_ball)
                div += len(aver_ball)
            return format(sum_b / div, '.1f')


print(reviewr1)
print(reviewr2)
print('------')
print(lector1)
print(lector2)
print('------')
print(student1)
print(student2)
print('------')
print(lector1 < lector2)
print(student1 < student2)
print(student2 < student1)

print(f"Средняя оценка студентам: {info_average_student('Python', student_list)}")
print(f"Средняя оценка лекторам: {info_average_lecturer('Python', lector_list)}")
