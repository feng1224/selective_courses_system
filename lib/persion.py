# -*-coding: utf-8 -*-
# Auther： Henry Yuan


class Persion(object):
    """Persion类"""

    def __init__(self):
        self.__name = None
        self.__sex = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        self.__name = value

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @age.setter
    def age(self, value):
        self.__age = value


class Teacher(Persion):

    def __init__(self):
        super(Teacher, self).__init__()


class Student(Persion):

    def __init__(self):
        super(Student, self).__init__()

    def register(self):
        pass
