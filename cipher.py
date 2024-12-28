result = ''
n = int(input('Введите число: '))
i = 1
j = 1
if n < 3 or n > 20:
    print('Число не подходит, введите число от 3 до 20')
else:
    while i <= n:
        j = 1
        while j <= n:
            if i < j and n % (i + j) == 0:
                result += str(i)
                result += str(j)
                j = j + 1
            else:
                j = j + 1
        i = i + 1
print('Ваш пароль: ', result)