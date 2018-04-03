# -*-coding: utf-8 -*-
# Auther： Henry Yuan
class Classes(object):

    def __init__(self):
        self.__name = None
        self.__course_obj = None
        self.__teacher_obj = None

    @property
    def name(self):
        return self.__name

    @property
    def course(self):
        return self.__course_obj

    @property
    def teacher(self):
        return self.__teacher_obj

    @name.setter
    def name(self, value):
        self.__name = value

    @course.setter
    def course(self, obj):
        self.__course_obj = obj

    @teacher.setter
    def teacher(self, obj):
        self.__teacher_obj = obj

    def setter(self, name, course, teacher):
        try:
            self.name = name
            self.course = course
            self.teacher = teacher
            return self
        except TypeError as e:
            print('\033[031;1m%s\033[0m'% e)
            return False