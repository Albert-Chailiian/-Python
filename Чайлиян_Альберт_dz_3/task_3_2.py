def num_translate(s):
    titles = 'OTFSEN'
    if s[0] in titles:
        s = s.lower()
        print(d.get(s).capitalize())
    else:
        print(d.get(s))


d = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
     'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
s = input('Введите числительное на англ языке от 0 до 10:')
num_translate(s)
