#Было интересно как сделать с datetime

from datetime import datetime
now=datetime.now()
dt_start=input('Введите дату дд.мм.гггг')
proshloe=datetime(1800,2,2)
try:
    dt_start=datetime.strptime((dt_start),'%d.%m.%Y')
except ValueError:
   print('Введен неверный формат')
while type(dt_start) == str:                 
    dt_start = input('попробуйте снова.')
    try:
      dt_start=datetime.strptime((dt_start),'%d.%m.%Y')
    except ValueError:
      print('Введен опять неверный формат')  
while type(dt_start) == datetime and dt_start> now or dt_start<proshloe:
    if dt_start > now:
       print('Леди и джентельмены,мы попали в будущее!')
    if dt_start< proshloe:
       print('Леди и джентельмены,мы попали в прошлое!')                    
    dt_start = input('попробуйте снова.')
    try:
      dt_start=datetime.strptime((dt_start),'%d.%m.%Y')
    except ValueError:
      print('Введен опять неверный формат')
      while type(dt_start) == str:
         dt_start= input('Попробуйте опять')
         try:
          dt_start=datetime.strptime((dt_start),'%d.%m.%Y')
         except ValueError:
          print('Введен опять неверный формат')   
v= ((now - dt_start)/365).days
print('Ваш возраст: ',v)
