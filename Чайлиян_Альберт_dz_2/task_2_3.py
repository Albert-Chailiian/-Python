a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for s in a:
    s = s.split(' ')
    print('Привет, ' + s[-1].capitalize() + '!')
