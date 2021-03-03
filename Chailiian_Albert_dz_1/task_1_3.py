def declination(procent):
    if procent == 1:
        print('1 процент')
    elif procent in (2, 3, 4):
        print(str(procent) + ' процента')
    else:
        print(str(procent) + ' процентов')


for i in range(21):
    declination(i)
