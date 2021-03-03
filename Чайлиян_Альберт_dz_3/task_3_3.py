def thesaurus(*args):
    d = {}
    for name in args:
        if name[0] in d.keys():
            d[name[0]].append(name)
        else:
            d.setdefault(name[0], [name])

    for k in sorted(d.keys()):
        print(k, d[k], sep='-')


thesaurus("Иван", "Мария", 'Милена', "Петр", 'Павел', "Илья", 'Ибрагим', "Альберт")
