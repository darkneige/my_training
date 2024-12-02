data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(data_structure)

def sum_calc(i):
    sum = 0
    if isinstance(i, (int, float)): #числа
        sum += i
    elif isinstance(i, str): #строки
        sum += len(i)
    elif isinstance(i, (list, tuple, set)): #списки, кортежи, множества
        for element in i:
            sum += sum_calc(element)
    elif isinstance(i, dict): #словари
        for key, value in i.items():
            sum = sum + sum_calc(value) + sum_calc(key)
    return sum


result = sum_calc(data_structure)
print(result)
