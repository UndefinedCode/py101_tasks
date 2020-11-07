#!/usr/bin/python3
"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

if __name__ == '__main__':
    def getZipAndZap(num):
        zip = num % 3 == 0
        zap = num % 5 == 0

        if zip and zap:
            return 'zip-zap'
        if zip:
            return 'zip'
        if zap:
            return 'zap'

        return num

    for num in range(1, 100):
        print(getZipAndZap(num))
