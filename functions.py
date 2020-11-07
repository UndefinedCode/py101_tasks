"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def task1(nums = input().split()):
    
    intList = [int(x) for x in nums]
    isEvevnNumber = False

    for x in intList:
        if (x % 2 == 0):
            isEvevnNumber = True

    if isEvevnNumber == True:
        print("Четные числа присутствуют!")
    else:
        print("Четных чисел нет.")    
    



# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
# age = 17
# sell_alcohol()
sell_alcohol() if age > 21 else "Мы не продаём алкоголь несовершеннолетним."


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
import keyword
def task2(keywordString = input()):
    for x in keyword.kwlist:
        if x == keywordString:
            print("Это ключевое слово")

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def task3(a):
    if isinstance(a, (int, float)):
        print("Является числом")
    if isinstance(a, str):
        print("Является строкой")
    if isinstance(a, bool):
        print("Булевый тип")
    if a is None:
        print("Тип 'None'")
    if isinstance(a, list):
        print("Массив")
    if isinstance(a, tuple):
        print("Кортеж")
    if isinstance(a, set):
        print("Множество")
    if isinstance(a, dict):
        print("Словарь")


        
    
