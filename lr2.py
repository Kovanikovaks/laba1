
password = input('Введите пароль:')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False

for char in password:
    if char.isnumeric():
        is_numeric = True
    elif char.isupper():
        is_upper = True
    elif char.islower():
        is_lower = True
    if char in "@$%^":
        is_spec = True

if len(password) > 5 and is_numeric and is_upper and is_lower and is_spec:
    print('Пароль подходит')
    password2 = input('Введите пароль ёще раз:')
    if password == password2:
        print('Пароль принят')
    else:
        print('Пароль не подходит')
elif len(password) <= 5:
    print('Пароль короткий')
elif not is_numeric:
    print('Пароль не подходит, добавьте цифры')
elif not is_upper:
    print('Пароль не подходит, добавьте верхний регистр')
elif not is_lower:
    print('Пароль не подходит, добавьте нижний регистр')
elif not is_spec:
    print('Пароль не подходит, добавьте спецзнаки')

