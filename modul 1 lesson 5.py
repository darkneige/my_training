#example 1
immutable_var = (1, "2", [3, 4], True) #создал переменную, присвоил кортеж из числа, строки, списка, функции
print(immutable_var)
#immutable_var[0]=5, immutable_var.remove('2'), immutable_var.extend (True, False) выдадут ошибку в коде из-за невозможности менять кортежи
immutable_var[2][0]=100 #я меняю не кортеж, а список,который содержится в кортеже, 2- номер элемента в кортеже, а 0- в списке
print(immutable_var)


#example 2
mutable_list= [1, '2', False]
print(mutable_list)
mutable_list[0]= mutable_list[0]*5 #домножил первый элемент на 5
print(mutable_list)
mutable_list[1]= int(mutable_list[1]) #изменил тип элемента со строки на число
print(mutable_list)
mutable_list.append(12) #добавил новый элемент в список
print(mutable_list)
mutable_list.remove(mutable_list[-1]) #убрал последний элемент списка
print(mutable_list)