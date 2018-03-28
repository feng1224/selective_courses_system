# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
from . import operators
from lib import views


def interactive(menu, menu_dict):
    """ 主菜单接口。
        用户首先登录主菜单，选择进入具体的通道。

    :return:
    """

    Flag = True
    while Flag:
        print(menu)
        cmd = input('>>:').strip()
        if cmd in menu_dict:
            return menu_dict[cmd]()
        else:
            print('选项不存在')
            return False


def homepage():
    menu = '''
    1. 学生登录通道
    2. 教师登录通道
    3. 管理员登录通道
    4. 退出
    '''
    menu_dict = {'1': views.StudentView,
                 '2': views.TeacherView,
                 '3': views.AdminView,
                 '4': logout}
    result = interactive(menu, menu_dict)
    return result

# @operators.login
# def student_channel():
#     menu = '''
#     1. 注册账号
#     '''
#     menu_dict = {'1': operators.registry}
#
#     interactive(menu, menu_dict)
#
# @operators.login
# def teacher_channel():
#     pass
#
# @operators.login
# def admin_channel():
#     menu = '''
#     1. 创建学校
#     '''
#     menu_dict = {'1': operators.create_school}
#
#     interactive(menu, menu_dict)


def logout():
    sys.exit()

def run():
    result = homepage()
    print(result)
    if result:
        result.homepage()
