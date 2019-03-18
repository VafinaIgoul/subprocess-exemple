# coding: utf-8
import sys


def add(first, second):
    u"""Возвращает сумму двух аргументов"""
    return first + second

if __name__ == '__main__':
    input_data = sys.stdin.readline()
    first, second = map(int, input_data.split(' '))
    result = str(add(first, second))
    sys.stdout.write(result)
