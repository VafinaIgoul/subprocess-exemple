# coding: utf-8
import sys


def exponentation(number):
    u"""Возвращает число, возведенное в степень"""
    return (number) ** 2

if __name__ == '__main__':
    input_data = sys.stdin.read()
    number = int(input_data)
    result = exponentation(number)
    sys.stdout.writelines((str(result), ' ', str(number)))
