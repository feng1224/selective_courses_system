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

    # def set_info(self, name, value):
    #     self.storage.nonquary(name, value)

    def __check_name(self, name):
        """ 检查方法
        1. 检查学校名称是否重复。

        :return:
        """
        if not os.path.exists('%s/%s' % (self.storage.db_path, name)):
            return True
        else:
            return False
