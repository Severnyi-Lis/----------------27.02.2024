#Написать программу, которая спрашивает возраст,
#выбрасывает исключение, если введенное число отрицательное,
#в противном случае считает год рождения.

#Сделал немножко не по заданию,без отрицательных чисел

age = input('Введите год рождения ')
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
while type(age)== int and age >2024 or age< 1924:
     if age > 2024:
      print('Леди и джентельмены,мы попали в будущее!')
     if age <1924:
       print('Леди и джентельмены,мы попали в прошлое!Где тут динозавры?')
     age=input('Введите правильный год рождения')
     try:
      age=int(age)
     except ValueError:
      print('Введен вообще неверный формат')
      while type(age) == str:
        age = input('попробуйте снова.')
        try:
         age=int(age)
        except ValueError:
         print('Введен опять неверный формат')
v=year-age
while  v<1 or type(age)==str:
   if v<1 and type(age)==int:
     print('Мало годиков...')
   age = input('попробуйте снова.')
   try:
    age=int(age)
    v=year-age  
   except ValueError:
    print('Введен опять 1 неверный формат') 
print('Ваш возраст: ',v)
