# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

from collections import Counter

temp = [i['first_name'] for i in students]
for k, v in Counter(temp).items():
    print(f'{k}: {v}')



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

from collections import Counter

temp = [i['first_name'] for i in students]
fin_name = ''
total = 0
for k, v in Counter(temp).items():
    if v > total:
        total = v
        fin_name = k
print(f'Самое частое имя среди учеников: {fin_name}')


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

#from collections import Counter
for students in range(len(school_students)):
    temp = [i['first_name'] for i in school_students[students]]
    fin_name = ''
    total = 0
    for k, v in Counter(temp).items():
        if v > total:
            total = v
            fin_name = k
    print(f'Самое частое имя в классе {students + 1}: {fin_name}')


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

for classes in school:
    temp = [i['first_name'] for i in classes['students']]
    m = 0
    f = 0
    for i in temp:
        if is_male[i]:
            m += 1
        else:
            f += 1
    print(f'Класс {classes["class"]}: девочки {f}, мальчики {m}')

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

fin_class_m = ''
total_m = 0
fin_class_f = ''
total_f = 0
for classes in school:

    temp = [i['first_name'] for i in classes['students']]
    m = 0
    f = 0
    for i in temp:
        if is_male[i]:
            m += 1
        else:
            f += 1
    if m > total_m:
        fin_class_m = classes["class"]
    if f > total_f:
        fin_class_f = classes["class"]

print(f'Больше всего мальчиков в классе {fin_class_m}\nБольше всего девочек в классе {fin_class_f}')
