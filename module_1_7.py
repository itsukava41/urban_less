immutable_var = 1, 2, 3, 'a', 'b', 'c'
print(immutable_var)
#immutable_var[0] = 2 - Объекты типа 'tuple' изменять нельзя. Обычнго кортежы используються,
#с данными котрые не подлежат изменению + кортеды занимают меньше места, чем списки.
mutable_list = ([1,3,5], 0,2, [4,'STRING'])
print(mutable_list)
mutable_list[0][0] = 3
print(mutable_list)
mutable_list[3][1] = 'Not STRING'
print(mutable_list)
