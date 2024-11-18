my_dict = {'Maksim': 28, 'Yaroslavna': 25, 'Vladislav': 29}
print(
    'Dict = ',
    my_dict)
print('Значение по ключу Maksim = ',
      my_dict['Maksim'])
print('Поучение по ключу Alexandr:', my_dict.get('Alexandr', 'Ключа нет!'))
my_dict.update({
    'Yarik':33,
    'Diana':31
})
print('Обновлённый Словарь:', my_dict)
a = my_dict.pop('Maksim'
)
print('Удалённое занчение по ключу Maksim = ', a)
print('Обновлённый Словарь v2 = :',my_dict)

set = {1, 2, 2, 4, 3, 7,5,7 ,7, 'Chiken', 3.14159}
print('Множество: ',set)
set.add('88737')
set.add(98)
set.remove('Chiken')
print('Новое множество: ',set)