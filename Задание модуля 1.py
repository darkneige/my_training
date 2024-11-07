grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#сортирую студентов по алфавиту + перевод  в список
students = sorted(students)
print ('Список студентов по алфавиту:', students)

#считаю среднюю оценку, где sum- сумма чисел в элементе списка, len - количество знаков в элементе списка
mean_grade = [ sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
print ('Средние оценки в классе:', mean_grade)

#ВАРИАНТ 1 (с помощью функции zip)
#для преобразования списка в словарь существует функция dict. чтобы два словаря преобразовать в словарь, использую функцию zip (объединение объектов)
print (dict(zip(students, mean_grade)))

#ВАРИАНТ 2  (с помощью ручного перечисления)
print ({students[0]: mean_grade[0], students[1]: mean_grade[1], students[2]: mean_grade[2], students[3]: mean_grade[3], students[4]: mean_grade[4]})

#ВАРИАНТ 3  (сокращенный способ)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print (dict(zip(sorted(students), mean_grade)))