# суть стека в том что каждый новый элемент добавляются в стек с конца, и он же первым забирается из стека
# В примере представлена программа проверки правильности и достаточности скобок в выражени

a = input('Введите строку: ')
stack = []
flVerify = True

for lt in a:
    if lt in '({[':
        stack.append(lt)
    elif lt in ')}]':
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

if flVerify and len(stack) == 0:
    print('Yes')
else:
    print('No')