def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
print_params(1, 2)

values_list_2 = [False, {'1': 2, '2': 3}]
values_dict = {'a': 12, 'b': "Слово", 'c': False}
print_params(*values_list_2, 42)
print_params(**values_dict)
