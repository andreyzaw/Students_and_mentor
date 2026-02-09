""" Functionality of the educational group.
Tracking of courses studied and completed,
grades assigned to students, and lecture grades"""
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Add finished courses
    def add_courses(self, course_name): 
        self.finished_courses.append(course_name)

# Grading lecturers
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Average score calculation
    def avg_grade(self):
        sum = 0
        count = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                sum += int(grade)
                count += 1
        if count > 0:
            result = sum / count
        else:
            result = 0
        return result

# Convert Student to string
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        result += f'\nСредняя оценка за домашние задания: {self.avg_grade()}'
        result += f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
        result += f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result

# Comparison ==
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() == other.avg_grade()
        return False

    # Comparison !=
    def __ne__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() != other.avg_grade()
        return False

    # Comparison <
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        return False

    # Comparison <=
    def __le__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() <= other.avg_grade()
        return False

    # Comparison >
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() > other.avg_grade()
        return False

    # Comparison >=
    def __ge__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() >= other.avg_grade()
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Average score calculation
    def avg_grade(self):
        sum = 0
        count = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                sum += int(grade)
                count += 1
        if count > 0:
            result = sum / count
        else:
            result = 0
        return result

    # Convert Lecturer to string
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        result += f'\nСредняя оценка за лекции: {self.avg_grade()}'
        return result

    # Comparison ==
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
        return False

    # Comparison !=
    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() != other.avg_grade()
        return False

    # Comparison <
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        return False

    # Comparison <=
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() <= other.avg_grade()
        return False

    # Comparison >
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() > other.avg_grade()
        return False

    # Comparison >=
    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() >= other.avg_grade()
        return False

class Reviewer(Mentor):
    # Grading student
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Convert Reviewer to string
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

def avg_student_course(students, course):
    sum = 0
    count = 0
    for student in students:
        if student.grades.get(course) != None:
            for grade in student.grades.get(course):
                sum += int(grade)
            count += len(student.grades.get(course))
    if count != 0:
        return sum / count
    return 0

def avg_lecturer_course(lecturers, course):
    sum = 0
    count = 0
    for lecturer in lecturers:
        if lecturer.grades.get(course) != None:
            for grade in lecturer.grades.get(course):
                sum += int(grade)
            count += len(lecturer.grades.get(course))
    if count != 0:
        return sum / count
    return 0



print(f"---------------- Инициализация  двух студентов ----------------------")
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Андрей', 'Антонов', 'М')
print(student1)
print("------------------------------")
print(student2)
print(f"---------------- Инициализация  двух лекторов ----------------------")
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Фёдор', 'Демьянов')
print(lecturer1)
print("------------------------------")
print(lecturer2)
print(isinstance(lecturer1, Mentor)) # True
print(isinstance(lecturer2, Mentor)) # True
print(lecturer1.courses_attached)    # []
print(lecturer2.courses_attached)    # []
print(f"---------------- Инициализация  двух экспертов ----------------------")
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Денис', 'Конев')
print(reviewer1)
print("------------------------------")
print(reviewer2)
print(isinstance(reviewer1, Mentor)) # True
print(isinstance(reviewer2, Mentor)) # True
print(reviewer1.courses_attached)    # []
print(reviewer2.courses_attached)    # []
print("-----------------------------------------------------")
# Adding courses students
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Git', 'Java']
student1.add_courses('Ручное тестирование Веб-приложений')
student2.add_courses('Ручное тестирование Веб-приложений')
print(student1)
print("------------------------------")
print(student2)
# Adding courses taught by mentor
lecturer1.courses_attached += ['Python', 'C++', 'Git']
lecturer2.courses_attached += ['Python', 'Java', 'Ручное тестирование Веб-приложений']
reviewer1.courses_attached += ['Python', 'C++', 'Java']
reviewer2.courses_attached += ['Git', 'Ручное тестирование Веб-приложений']
# Adding grades for lectures
print(student1.rate_lecture(lecturer1, 'Python', 7))   # None
print(student2.rate_lecture(lecturer2, 'Java', 8))     # None
print(student1.rate_lecture(lecturer1, 'С++', 8))      # Ошибка
print(student1.rate_lecture(reviewer1, 'Python', 6))   # Ошибка
print(student1.rate_lecture(lecturer1, 'Git', 9))   # None
print(student2.rate_lecture(lecturer1, 'Git', 6))   # None
print(lecturer1.grades)  # {'Python': [7], 'Git': [9, 6]}
print(lecturer2.grades)  # {'Java': [8]}
print("------------------------------")
print(lecturer1)
print(lecturer2)
print("------------------------------")
print(reviewer1.rate_hw(student1,'Python', 10))                                  # None
print(reviewer2.rate_hw(student1,'Git', 9))                                      # None
print(reviewer1.rate_hw(student1,'Python', 10))                                  # None
print(reviewer1.rate_hw(student1,'Ручное тестирование Веб-приложений', 8))       # Ошибка
print(reviewer2.rate_hw(student2,'Git', 8))                                      # None
print(reviewer2.rate_hw(student1,'Ручное тестирование Веб-приложений', 8))       # Ошибка
print(student1.grades)
print(student2.grades)
print("------------------------------")
print(student1)
print("------------------------------")
print(student2)
# compare
print(student1 == student2) # False
print(student1 != student2) # True
print(student1 >= student2) # True
print(student1 > student2)  # True
print(student1 <= student2) # False
print(student1 < student2)  # False
print("------------------------------")
print(lecturer1 == lecturer2) # False
print(lecturer1 != lecturer2) # True
print(lecturer2 <= lecturer1) # False
print(lecturer2 < lecturer1) # False
print(lecturer2 >= lecturer1) # True
print(lecturer2 > lecturer1) # True

list_student = [student1, student2]
print(avg_student_course(list_student,'Git'))

list_lecturer = [lecturer1, lecturer2]
print(avg_lecturer_course(list_lecturer,'Git'))