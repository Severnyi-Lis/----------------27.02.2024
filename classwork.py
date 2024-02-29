#Классная работа
znam = input('Введите число: ')  
try:
    znam = int(znam)
except ValueError: 
    print('Вы ввели не число')
while type(znam) == str or znam == 0:
    if znam == 0:
        print('На ноль делить нельзя!')
    znam = input('попробуйте снова.')
    try:
        znam = int(znam)
    except ValueError:
        print('Вы опятьввели не число')
result = 1 / znam
print('Обратное равно', result)
