my_dict = {'Ivan': 1990, 'Masha': 1995, 'Igor': 1993, 'Ruslan': 1992}
print(my_dict)
print(my_dict.get('Igor'))
print(my_dict.get('Vova', 'Такого имени нет'))
my_dict.update({'Dima': 2002,
                'Lena': 2005})
my_dict.pop('Ruslan')
print(my_dict)

my_set = {1, 10, 100, 1000, 1, 10, 100, 1000}
print(my_set)
my_set.add('Hot')
my_set.add((5, 50, 500))
my_set.remove(1000)
print(my_set)
