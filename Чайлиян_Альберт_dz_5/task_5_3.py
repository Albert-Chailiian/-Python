tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = [
    '9А', '7В', '9Б', '9В']

''' если длина klasses меньше, то добавляем в конец списка столько None,
сколько составляет разница в длине между 2-мя списками'''

for i in range(0, len(tutors) - len(klasses)):
    klasses.append(None)

'''формируем кортежи с помощью zip'''
zz = ((t, k) for t, k in zip(tutors, klasses))
print(zz)
print(*zz)
