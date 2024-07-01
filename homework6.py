my_dict = {'Ivan': 1990, 'Masha': 1995, 'Igor': 1993, 'Ruslan': 1992}
print(my_dict)
print(my_dict['Igor'])
my_dict['Igor'] = 2000
print(my_dict['Igor'])
print(my_dict)
my_dict['Dima'] = 2002
my_dict['Lena'] = 2005
print(my_dict)
del my_dict['Ivan']
print(my_dict)

my_set = {1, 10, 100, 1000, 1, 10, 100, 1000}
print(my_set)
my_set.add('Hot')
my_set.add((5, 50, 500))
my_set.remove(1000)
print(my_set)
