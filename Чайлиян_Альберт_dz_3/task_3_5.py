from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=5, distinct_words=1):
    """ В пустой список добавляем n раз строки, состоящие их случайно выбранных слов из трех заданных списков для флага = 0.
     флаг distinct_words =1 запрещает использовать любое слово из трех списков два раза.
     n задает кол-во выводимых шуток, по умолчанию = 5. проверку на больше n большее 5 не устанавливал
     можно было бы реализовать через удаление выбранных слов из списка, но я решил посложнее - с while и choice"""
    if distinct_words == 1:
        jokes_list = []
        joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        jokes_list.append(joke)
        for i in range(n - 1):
            jokes = ''.join(jokes_list)
            first = ''
            while first in jokes:
                first = choice(nouns)
            second = ''
            while second in jokes:
                second = choice(adverbs)
                if jokes.count('позавчера') == 1 and jokes.count('вчера') == 1 and second == 'вчера':
                    break
            third = ''
            while third in jokes:
                third = choice(adjectives)
            joke1 = first + ' ' + second + ' ' + third
            jokes_list.append(joke1)
        print(jokes_list)
    else:
        jokes_list = []
        for i in range(n):
            joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
            jokes_list.append(joke)
        print(jokes_list)


get_jokes(5, 1)
