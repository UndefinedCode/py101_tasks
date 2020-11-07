#!/usr/bin/python3
import re
"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    password = input('Ваш пароль: ')
    staticmetArr = [
        len(password) >= 8,
        re.search('[0-9]', password) is not None,
        re.search('(?i)[a-z]', password) is not None
    ]

    for staticmet in staticmetArr:
        if not staticmet:
            print('Пароль небезопасен')
            raise SystemExit

    print('Пароль безопасен!')
