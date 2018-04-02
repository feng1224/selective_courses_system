# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import schools
from lib import accounts
import sys

def login(func):
    """ 登录函数

    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        if args[0].login():
            func(*args, **kwargs)
    return inner


def sign_up(obj):
    """ 注册函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.register()
    return True


@login
def change_password(obj):
    """ 修改账号的密码

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.change_password()
    return True


@login
def set_information(obj):
    """ 设置账号信息函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.set_info()
    return True


@login
def tell_information(obj):
    """ 查看账户信息函数

    :param obj: 传入需要的视图对象
    :return:
    """
    result = obj.tell_info()
    print(result)
    return 'haha'


@login
def choice_course(obj):
    """ 选择课程函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.choise_courses()
    return True


@login
def tell_record(obj):
    """ 查看学习记录函数

    :param obj: 传入需要的视图对象
    :return:
    """
    pass


def sign_out(obj):
    """ 注销函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.logout()
    return False


def exit_system():
    """ 退出系统函数

    :return:
    """
    print('\033[34;1m欢迎使用本系统，下次再见！\033[0m')
    sys.exit()

@login
def create_school(obj):
    """ 创建学校函数

    :param obj: 传入需要的视图对象
    :return:
    """
    pass


@login
def create_courses(obj):
    pass


@login
def create_classes(obj):
    pass


def create_teachers(obj):
    pass


@login
def create_students(obj):
    pass