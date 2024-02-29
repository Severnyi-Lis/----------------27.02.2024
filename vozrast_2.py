#Написать программу, которая спрашивает возраст,
#выбрасывает исключение, если введенное число отрицательное,
#в противном случае считает год рождения.

age = input('Введите возраст ')
year=2024
try:
    age=int(age)
except ValueError:
   print('Введен неверный формат')
while type(age) == str:                 
    age = input('попробуйте снова.')
    try:
      age=int(age)
    except ValueError:
      print('Введен опять неверный формат')  
while type(age) == int and age< 0:
    if age < 0:
       print('Кажется у вас отрицательный возраст....')                 
    age = input('попробуйте снова.')
    try:
      age=int(age)
    except ValueError:
      print('Введен опять неверный формат')
      while type(age) == str:
         age= input('Попробуйте опять')
         try:
          age=int(age)
         except ValueError:
          print('Введен опять неверный формат')   
v= year-age
print('Ваш год рождения: ',v)


