def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input('Количество строк матрицы :'))
m = int(input('Количество столбцов матрицы :'))
value = input(f'Значение : ')
print('-------' * m)
matrix = get_matrix(n, m, value)    # Выведите на экран(консоль) результат работы функции get_matix.

print("Матрица воплоти:")
for i in matrix:
    print(*i)