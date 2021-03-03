a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(a):
    if a[i].isdigit():
        if int(a[i]) < 10:
            a[i] = '0' + a[i]
    if a[i].startswith('+'):
        a[i] = a[i].replace('+', '+0')

    i = i + 1
j = 0
while j < len(a):
    if a[j].isdigit() or a[j].startswith('+'):
        a = a[0:j] + ['\"', a[j], '\"'] + a[j + 1:]
        j = j + 3
    else:
        j = j + 1

s = ''
k = 0
while k < len(a):
    if not (a[k].isdigit() or a[k].startswith('+')):
        if a[k] == '\"':
            s = s + a[k]
        else:
            s = s + a[k] + ' '
        k = k + 1
    else:
        s = s + a[k] + '\"' + ' '
        k = k + 2
print(s)
