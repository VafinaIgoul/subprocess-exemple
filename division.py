# coding: utf-8
import sys


def division(first, second):
    u"""Возвращает деление первого числа на второе."""
    return first / second

if __name__ == '__main__':
    input_data = sys.stdin.readline()
    first, second = map(int, input_data.split(' '))
    try:
        result = str(division(first, second))
    except ZeroDivisionError:
        result = '0 is one of arguments!'
    sys.stdout.write(result)
