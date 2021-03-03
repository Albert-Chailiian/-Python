a = [45, 87.07, 65.4, 99.09, 4.04, 1899, 10.01, 99.99, 20.09, 15.54, 21.34, 86.34, 98, 4.67, 13.85, 17.17]
print(f'ID{id(a)} списка {a}')
a.sort()
print('after sort()')
print(f'ID{id(a)} списка {a}\n')

'''выводим топ5 цен одной строкой'''

print('TOP_5 prices', *sorted(a, reverse=True)[0:6], sep='||')
