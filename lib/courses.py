# -*-coding: utf-8 -*-
# Auther： Henry Yuan


class Courses(object):

    def __init__(self):
        self.__name = None
        self.__price = None
        self.__period = None

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def period(self):
        return self.__period

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError('Error: Course name [%s] must be str' % value)

    @price.setter
    def price(self, value):
        if isinstance(value, int):
            self.__price = value
        else:
            raise TypeError('Error: Course price [%s] must be int' % value)

    @period.setter
    def period(self, value):
        if isinstance(value, int):
            self.__period = value
        else:
            raise TypeError('Error: Course period [%s] must be int' %value)

    def setter(self, name, price, period):
        try:
            self.name = name
            self.price = price
            self.period = period
            return self
        except TypeError as e:
            print('\033[031;1m%s\033[0m'% e)
            return False

    # def getter(self):
    #     return self

if __name__ == '__main__':
    test = Courses()
    test.setter('hen','12','213')
    print(test.name)
    print(test.getter().__dict__)

