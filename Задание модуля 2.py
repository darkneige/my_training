def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password = password + str(i) + str(j)
    return password

number = int(input('Введите целое число от 3 до 20: '))
result = get_password(number)
print('Пароль:', result)