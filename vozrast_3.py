#Было интересно как сделать с datetime,но времени не хватило 


from datetime import datetime
now=datetime.now()
dt_start=''

try:
    dt_start=datetime.strptime(input('Введите дату дд.мм.гггг'),'%d.%m.%Y')
except ValueError:
   print('Введен неверный формат')
while type(dt_start) == str:                 
    dt_start = input('попробуйте снова.')
    try:
      dt_start=datetime.strptime(input('Введите дату дд.мм.гггг'),'%d.%m.%Y')
    except ValueError:
      print('Введен опять неверный формат')  
while type(dt_start) == datetime and dt_start> now:
    if dt_start > now:
       print('Леди и джентельмены,мы попали в будущее!')                 
    dt_start = input('попробуйте снова.')
    try:
      dt_start=datetime.strptime(input('Введите дату дд.мм.гггг'),'%d.%m.%Y')
    except ValueError:
      print('Введен опять неверный формат')
      while type(dt_start) == str:
         dt_start= input('Попробуйте опять')
         try:
          dt_start=datetime.strptime(input('Введите дату дд.мм.гггг'),'%d.%m.%Y')
         except ValueError:
          print('Введен опять неверный формат')   
v= ((now - dt_start)/365).days
print('Ваш возраст ',v)
