if len(s) > 5:
    for i in s:
        if i in ['@', '#', '%', '&']:
            count[0] += 1
        elif i.isupper():
            count[1] += 1
        elif i.isdigit():
            count[2] += 1
 
    if count[1] < 1:
        print('Пароль должен содержать буквы в верхнем регистре')
    elif count[2] < 1:
        print('Пароль должен содержать цифры')
    elif count[0] < 1:
        print('Пароль должен содержать символы @, #, %, &')
    else:
        print('Хороший пароль')
else:
    print('Длина пароля должна быть больше 5 символов')