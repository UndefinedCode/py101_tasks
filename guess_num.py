"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random
randomNumber = random.randrange(0, 1000000)
hello = "Вас приветствует 'Рандомотрон-3000', загадайте ваше число от 0 до 1000000: "
userNumber = input(hello)

if (userNumber == "exit" or userNumber == ""):
    raise SystemExit

if userNumber.isdigit() == False:
    print("Вы ввели не число или отрицательное число")
    raise SystemExit

integerUserNumber = int(userNumber)

if (integerUserNumber < 0 or integerUserNumber > 1000000):
    print("Число не входит в допустимый диапазон")
    raise SystemExit

if (integerUserNumber < randomNumber):
    print("Загаданное число меньше случайного")

if (integerUserNumber > randomNumber):
    print("Загаданное число больше случайного")

if (integerUserNumber == randomNumber):
    print("Поздравляем, вы угадали число!")
