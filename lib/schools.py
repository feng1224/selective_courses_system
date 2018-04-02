# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import db
from conf import settings
import os


class Schools(object):
    """ 学校类 """
    storage = db.inter_db_handler(settings.BASE_DATABASE)

    def __init__(self):
        self.name = None
        self.city = None
        self.location = None
        self.course_list = None
        self.class_list = []
        self.teacher_list = []
        self.student_list = []

    def setter(self, name, city, location):
        """ 创建学校方法

        :param name:
        :param city:
        :param location:
        :return:
        """
        if self.__check_name(name):
            self.name = name
            self.city = city
            self.location = location
            return self
        else:
            return False

    def getter(self, name):
        """ 获取学校方法

        :return:
        """
        if self.__check_name(name):
            return False
        else:
            return self.storage.quary(name)

    def create_school(self, name, value):
        print(value)
        self.storage.nonquary(name, value)
    # def tell_school(self):
        #pass

    def __check_name(self, name):
        """ 检查方法
        1. 检查学校名称是否重复。

        :return:
        """
        print(self.storage.db_path, name)
        if not os.path.exists('%s/%s' % (self.storage.db_path, name)):
            return True
        else:
            return False

    def set_courses(self, school, course_obj):
        result = self.getter(school)
        if result:
            print(result.__dict__)
            result.course_list[course_obj] = course_obj
            print(result.__dict__)
        else:
            return False
        #self.storage.nonquary(self)


if __name__ == '__main__':
    test = Schools()
    print(test.getter('sh'))
    print(test.set_courses('sh','haha'))
    print(test.set_courses('sh', 'haha1'))