'''Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.'''

duration = int(input('Введите промежуток времени в секундах:'))
if duration >= 86400:
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    print('Это ' + str(duration // 86400) + ' сут., ' + str(hours) + ' час., ' + str(minutes) + ' мин., ' + str(
        duration % 60) + ' сек.')
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    print('Это ' + str(hours) + ' час., ' + str(minutes) + ' мин., ' + str(duration % 60) + ' сек.')
else:
    minutes = duration // 60
    print('Это ' + str(minutes) + ' мин., ' + str(duration % 60) + ' сек.')
