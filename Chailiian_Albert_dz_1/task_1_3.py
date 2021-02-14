procent = int(input('Введите число от 0 до 20 для определения склонения к слову \'процент\':'))
if not 0 <= procent <= 20:
    print('Вы ввели число вне диапазона 0-20\nПопробуйте еще раз.')
elif procent == 1:
    print('1 процент')
elif procent in (2, 3, 4):
    print(str(procent) + ' процента')
else:
    print(str(procent) + ' процентов')
