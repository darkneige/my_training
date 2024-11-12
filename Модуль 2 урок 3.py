# Вариант 1.1 (через break)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
arg = 0
while my_list[arg] >= 0 or arg < len(my_list):
    if my_list[arg] > 0:
        print(my_list[arg])
        arg += 1
    elif my_list[arg] < 0:
        arg += 1
    else:
        break

# Вариант 1.2 (через break)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
arg = 0
while arg < len(my_list):
    if my_list[arg] < 0:
        break
    if my_list[arg] > 0:
        print(my_list[arg])
    arg += 1

# Вариант 2 (через continue)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
arg = 0
while my_list[arg] >= 0 or arg < len(my_list):
    if my_list[arg] > 0:
        print(my_list[arg])
        arg += 1
    elif my_list[arg] == 0:
        arg += 1
        continue
