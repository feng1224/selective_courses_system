# -*-coding: utf-8 -*-
# Auther： Henry Yuan
class Schools(object):
    """ 学校类 """

    def __init__(self):
        self.__name = None
        self.__city = None
        self.__location = None
        self.__course_list = []
        self.__class_list = []
        self.__teacher_list = []
        self.__student_list = []

    def setter(self, name, city, location):
        """ 添加学校方法

        :param name:
        :param city:
        :param location:
        :return:
        """
        # if not name or not city or not location:
        #     return False
        setter_result = False
        if self.__check(name, city):
            self.__name = name
            self.__city = city
            self.__location = location
            return self
        else:
            return False

    @property
    def getter(self):
        """ 获取学校方法

        :return:
        """
        return self.__name, self.__city, self.__location

    def __check(self, *args):
        """ 检查方法
        1. 检查学校名称是否重复。

        :return:
        """
        print(args)
        return True