a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

m, n = a, b
if m == n:
    print(f'Нод чисел {a} и {b}: {m}')
elif m == 0 or n == 0:
    print(f'Нод чисел {a} и {b}: 0')
else:
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    print(f'Нод чисел {a} и {b}: {m}')