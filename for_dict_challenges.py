# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
import pprint
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
flat_stud_list = [student.get('first_name') for student in students]
for name in set(flat_stud_list):
     print(f'{name}: {flat_stud_list.count(name)}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
flat_stud_list = [student.get('first_name') for student in students]
print(f'Самое частое имя среди учеников: {max(flat_stud_list, key=flat_stud_list.count)}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i, students in enumerate(school_students):
    flat_stud_list = [student.get('first_name') for student in students]
    print(f'Самое частое имя в классе {i + 1}: {max(flat_stud_list, key=flat_stud_list.count)}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

# Читаемое решение
# flat_stud_list = [students.get('students') for students in school]
# class_list = [students.get('class') for students in school]
# for i, students in enumerate(flat_stud_list):
#     male = 0
#     female = 0
#     for student in students:
#         if is_male.get(student.get("first_name")): 
#             male += 1
#         else: 
#             female += 1
#     print(f'Класс {class_list[i]}: девочки {female}, мальчики {male}')

# Компактное решение
for i, students in enumerate([students.get('students') for students in school]):
    genders = ['male' if is_male.get(student.get("first_name")) else 'female' for student in students]
    print(f'Класс {[students.get("class") for students in school][i]}: девочки {genders.count("female")}, мальчики {genders.count("male")}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
result = []
for i, students in enumerate([students.get('students') for students in school]):
    # print(f'Класс {i} со студентами {students}') 
    genders = ['male' if is_male.get(student.get("first_name")) else 'female' for student in students]
    # print(f'Класс {i} со студентами, где пол студентов {genders}')
    result.append(([students.get('class') for students in school][i], genders.count('male'), genders.count('female')))
    # print(f'В классе {[students.get("class") for students in school][i]}: {genders.count("male")} мальчиков и {genders.count("female")} девочек')
print(f'Больше всего мальчиков в классе {max(result, key=lambda i : i[1])[0]}')
print(f'Больше всего девочек в классе {max(result, key=lambda i : i[2])[0]}')