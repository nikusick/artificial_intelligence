"""Создайте класс по работе с тригонометрическими функциями. В классе
должны быть реализованы функции вычисления:
− косинуса;
− синуса;
− тангенса;
− арксинуса;
− арккосинуса;
− арктангенса;
− перевода из градусов в радианы.
"""
import math


class Trigonometry:

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def tan(x):
        return math.tan(x)

    @staticmethod
    def asin(x):
        return math.asin(x)

    @staticmethod
    def acos(x):
        return math.acos(x)

    @staticmethod
    def atan(x):
        return math.atan(x)

    @staticmethod
    def radians(x):
        return math.radians(x)
