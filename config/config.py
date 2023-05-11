class MainLink:
    link = 'https://www.joompers.com/'


class LoginPageData:
    valid_email = 'bad@mail.ru'
    valid_password = 'QwErQwEr'


class RegisterPageData:
    valid_email = 'testfir@mail.ru'
    valid_password = 'QwErQwEr'


class InvalidRegisterData:
    invalid_symbols_1 = r'\/<>()[]@,;:"*&=+'
    invalid_symbols_2 = '_-.'
    the_gap = ' '
    invalid_emails_1 = [
                           f'{x}blabla@mail.ru' for x in invalid_symbols_1 + invalid_symbols_2
                           # Локальная часть начинается с inv_smb
                       ] + [
                           f'bla{x}bla@mail.ru' for x in invalid_symbols_1 + the_gap  # Локальная часть содержит inv_smb
                       ] + [
                           f'blabla{x}@mail.ru' for x in invalid_symbols_1 + invalid_symbols_2 + the_gap
                       ] + [
                           f'blabla@{x}mail.ru' for x in invalid_symbols_1 + invalid_symbols_2 + the_gap
                       ] + [
                           f'blabla@ma{x}il.ru' for x in invalid_symbols_1 + the_gap  # Доменная часть содержит inv_smb
                       ] + [
                           f'blabla@mail.ru{x}' for x in invalid_symbols_1 + invalid_symbols_2
                           # Доменная часть заканчивается inv_smb
                       ] + [
                           '',  # пустое поле
                           'blab@mail.ru',  # Менее 5 символов в локальной части
                           'BLABLA@mail.ru',  # Верхний регистр
                           'блабла@mail.ru',  # Кириллица
                           'blablamail.ru',  # Отсутствие @ в email
                           '@mail.ru',  # Отсутствие локальной части
                           'blabla',  # Отсутствие доменной части
                           'blabla@mail..ru'  # Содержит две точки подряд
                       ]

    invalid_emails_2 = [
        'qwertyuiopasdfghjklpzxcvbnmklpqwertyuiopasdfghjklpzxcvbnmklpqweer@mail.ru',  # Превышение локальной части
        'f@qwertywuiopasdfghjklzxcvbnmqwertyuiopasdfgwhjklzxcvbnmqwertyuiop.ru'  # Превышение доменного имени
    ]

    invalid_passwords = [
        '',  # Пустой пароль
        '!wErQw1',  # Меньше минимально допустимого
        'ЙцУкЙцУк',  # Только кириллица
        'password',  # Только нижний регистр
        'PASSWORD',  # Только верхний регистр
        '12№4word',  # Без верхних регистров
        '12№4WORD',  # Без нижних регистров
        '12341234',  # Только цифры
        'PASsWOR!',  # Без цифр
        '!@#$!@#$',  # Только спецсимволы
        'PAs43ord',  # Без спецсимволов
        '12345678901234!We'  # Более 16 символов в пароле
    ]


class InvalidLoginData:
    invalid_emails = [
        'naprimer@mail.ru',                 # Другой емейл
        LoginPageData.valid_email.upper()   # Валидный логин в верхнем регистре
    ]

    invalid_passwords = [
        'AsD1!sDf',     # Другой пароль
        ''              # Пустое поле
    ]


class EditProfile:
    valid_names = [
        'Edward',
        'EDWARD',
        'Karl-Marks',
        'Karl Marks',
        "D'artagnan",
        'L',             # 1 symbol
        'QWERwEWQWTYUIOPQWERTQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOP'     # 100
    ]
    invalid_names = [
        '',
        'Эдуард',
        '1234',
        '!@#$',
        'qQWERTYUIeeeweOPPOASeDFGqweqweqweHJKLZXCVBNMQWERTYUIQWERTYUIOPPOASDFGHJKLZXCVBNMOPPOASDFGHJKLZXCVBNMQ'    # 101
    ]
    valid_nicknames = [
        'QWEQWEQWEQQWEQWEQWEQQWEQWEQWEQQQ',         # 32 symbol (MAX)
        '12345',                                    # only numbers
        'RAT',                                      # 3 symbol (MIN)
        'qwertq'                                    # low symbols
    ]
    invalid_nicknames = [
        'RD',                                       # 2 symbol (MIN = 3)
        '!23wQ',                                    # spec symbol
        'ЙЦУК',                                     # russian symbols
        "йцук",                                     # low russian symbols
        'QWEQWEQWEQQWEQWEQWEQQWEQWEQWEQQQQ',        # 33 symbols (MAX = 32)
        ''                                          # empty
    ]
    valid_bio = [
        '',
        'One, two, three, four, five, six, seven, BLABLABALBALABALBALBALBALBA 11, 12, 13, 14, !%.'
        ' MOR, eqwDAY!!"№;%:?*()_+{}[]":;<>.,?/""ZFASDQWEFZZS'      # 140 symbols (MAX)
    ]
    invalid_bio = [
        'One, two, three, four, five, six, seven, BLABLABALBALABLABALBALBALBALBA 11, 12, 13, 14, !%. MOR, FRIDAY!'
        '!"№;%:?*()_+{}[]":;<>.,?/""EQWEQWEQE1',     # 141 symbols (MAX = 140)
        'Русский'
    ]
