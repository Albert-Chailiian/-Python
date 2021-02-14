def summaDigits(n):
    _sum = 0
    while n != 0:
        ostatok = n % 10  # от деления на 10, таким образом находим последнюю цифру n
        _sum += ostatok
        n = n // 10  # отбрасываем последнюю цифру
    return _sum


a = []
for i in range(1001):
    if not i % 2 == 0:
        a.append(i ** 3)
sum = 0
for elem in a:
    if summaDigits(elem) % 7 == 0:
        sum += elem
print(a)
print(sum)
sum17 = 0
for i in range(len(a)):
    a[i] = a[i] + 17
    if summaDigits(a[i]) % 7 == 0:
        sum17 += a[i]
print(a)
print(sum17)
