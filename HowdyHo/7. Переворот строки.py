import string

str = 'эту строку надо развернуть;'
ln = len(str)
print(str)
chars = list(str)

str = str[::-1]  # Самый простой и лучший вариант

# Превращаем строку в список и меняем символы, затем вновь обьединяем в строку
for i in range(ln//2-1):
    chars[i], chars[ln-i-1] = chars[ln-i-1], chars[i]

print('********')
print(str)
print('********')
print(''.join(chars))
