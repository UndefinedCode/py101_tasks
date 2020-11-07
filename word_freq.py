#!/usr/bin/python3
"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import nltk
from nltk.corpus import stopwords

if __name__ == '__main__':
    path = input('Введите путь до файла:')
    file = open(path, 'r')
    str = file.read()
    wordsArr = str.split()
    result = {}

    for i in range(len(wordsArr)):
        word = wordsArr[i]
        last = word[len(word) - 1]
        splitArg = ['.', ',', '!', '?', ')', '(']

        if last in splitArg:
            wordsArr[i] = wordsArr[i].replace(last, '')

    for word in wordsArr:
        stopwordsArr = stopwords.words('russian')

        if word not in stopwordsArr and not word.isdigit():
            loverWords = word.lower()
            if loverWords in result:
                result[loverWords] = result[loverWords] + 1
            else:
                result[loverWords] = 1

    topWord = []

    def sort(arr):
        if len(arr) != 0:
            top = {'name': '', 'count': 0}

            for word in arr.keys():
                if result[word] > top['count']:
                    top = {'name': word, 'count': result[word]}

            del arr[top['name']]
            topWord.append(top['name'])
            sort(arr)
    sort(result)

    index = 0
    for word in topWord:
        index += 1

        if index <= 100:
            print(u'Топ-{} {}'.format(index, word))
