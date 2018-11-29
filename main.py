print('Я хочу сыграть с тобой в игру...')
print('...в города')
import random
a = random.randint(1,2)
goroda = open('Baza_gorodov (1).txt').readlines()
otrabotka = []
stop = 'я больше так не могу, пожалуйста хватит!'
count = 0
if a == 1:
    print('Ты ходишь первый!')
    while True:
        a = input()
        if a not in (otrabotka) and a.title()+'\n' in (goroda):
            otrabotka.append(a)
            count += 1
            if a[-1] == 'ь' or a[-1] == 'ъ':
                for b in (goroda):
                    if b[0].lower() == a[-2] and b.lower()[:-1] not in (otrabotka):
                        break
                    else:
                        continue
            else:
                for b in (goroda):
                    if b[0].lower() == a[-1] and b.lower()[:-1] not in (otrabotka):
                        break
                    else:
                        continue
            otrabotka.append(b.lower())
            print(b)
            break
        else:
            print('Попробуй ещё раз, глупый кожаный мешок')


    while True:
        a = input()
        if a == stop :
            break
        if b[-2] == 'ь' or b[-2] == 'ъ' :
            if a not in (otrabotka) and a.title() + '\n' in (goroda) and a[0].lower() == b[-3]:
                otrabotka.append(a.lower())
                count += 1
                if a[-1] == 'ь' or a[-1] == 'ъ':
                    for b in (goroda):
                        if b[0].lower() == a[-2] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                else :
                    for b in (goroda):
                        if b[0].lower() == a[-1] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                otrabotka.append(b.lower()[:-1])
                print(b)
            else:
                print('Попробуй-ка ещё раз, глупый кожаный мешок')
        else:
            if a not in (otrabotka) and a.title() + '\n' in (goroda) and a[0].lower() == b[-2]:
                otrabotka.append(a.lower())
                count += 1
                if a[-1] == 'ь' or a[-1] == 'ъ':
                    for b in (goroda):
                        if b[0].lower() == a[-2] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                else :
                    for b in (goroda):
                        if b[0].lower() == a[-1] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                otrabotka.append(b.lower()[:-1])
                print(b)
            else:
                print('Попробуй-ка ещё раз, глупый кожаный мешок')

else:
    print('Компьютер ходит первый!')
    b = random.choice(goroda)
    otrabotka.append(b.lower()[:-1])
    print(b)

    while True:
        a = input()
        if a == stop :
            break
        if b[-2] == 'ь' or b[-2] == 'ъ' :
            if a not in (otrabotka) and a.title() + '\n' in (goroda) and a[0].lower() == b[-3]:
                otrabotka.append(a.lower())
                count += 1
                if a[-1] == 'ь' or a[-1] == 'ъ':
                    for b in (goroda):
                        if b[0].lower() == a[-2] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                else :
                    for b in (goroda):
                        if b[0].lower() == a[-1] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                otrabotka.append(b.lower()[:-1])
                print(b)
            else:
                print('Попробуй-ка ещё раз, глупый кожаный мешок')
        else:
            if a not in (otrabotka) and a.title() + '\n' in (goroda) and a[0].lower() == b[-2]:
                otrabotka.append(a.lower())
                count += 1
                if a[-1] == 'ь' or a[-1] == 'ъ':
                    for b in (goroda):
                        if b[0].lower() == a[-2] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                else :
                    for b in (goroda):
                        if b[0].lower() == a[-1] and b.lower()[:-1] not in (otrabotka):
                            break
                        else:
                            continue
                otrabotka.append(b.lower()[:-1])
                print(b)
            else:
                print('Попробуй-ка ещё раз, глупый кожаный мешок')


print('Игра окончена, ваш счет')
print(count)