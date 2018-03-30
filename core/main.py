# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
from lib import views
from lib import accounts

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


student_view = views.StudentView()
teacher_view = views.TeacherView()
def interactive(menu, menu_dict, obj):
    """ 主菜单接口。
        用户首先登录主菜单，选择进入具体的通道。

    :return:
    """

    Flag = True
    while Flag:
        print(menu)
        cmd = input('>>:').strip()
        if cmd in menu_dict:
            eval(menu_dict[cmd])
        else:
            print('选项不存在')

def homepage(obj=None):
    menu = '''
===============欢迎进入老男孩学校===============
                1. 学生登录通道
                2. 教师登录通道
                3. 管理员登录通道
                4. 退出
================================================
    '''
    menu_dict = {'1': 'student_homepage()',
                 '2': 'views.TeacherView()',
                 '3': 'views.AdminView()',
                 '4': 'exit()'}
    result = interactive(menu, menu_dict,obj)
    return result

def student_homepage(obj=student_view):

    menu = '''
===============欢迎进入学员视图===============
               1. 注册账号
               2. 填写个人信息
               3. 查看账户信息
               4. 选择课程并付费
               5. 查看学习记录
               6. 注销
==============================================
    '''
    menu_dict = {'1': 'register(obj)',
                 '2':  'set(obj)',
                 '3': 'tell(obj)',
                 '4': 'choise(obj)',
                 '5': 'record(obj)',
                 '6': 'logout(obj)'}
    interactive(menu, menu_dict, obj)

def teacher_homepage(obj=teacher_view):

    menu = '''
===============欢迎进入学员视图===============
               1. 注册账号
               2. 补充个人信息
               3. 查看账户信息
               4. 选择课程
==============================================
    '''
    menu_dict = {'1': 'register(obj)',
                 '2':  'set(obj)',
                 '3': 'tell(obj)',
                 '4': 'choise_pay(obj)'}
    interactive(menu, menu_dict, obj)

def login(func):
    """ 登录函数

    :param func:
    :return:
    """
    def inner(*args,**kwargs):
        if args[0].login():
            func(*args,**kwargs)
    return inner

def register(obj):
    obj.register()

@login
def set(obj):
    obj.set_info()


@login
def tell(obj):
    obj.tell_info()
    #print(obj.__dict__)


def logout(obj):
    obj.logout()

def exit():
    print('\033[34;1m欢迎使用本系统，下次再见！\033[0m')
    sys.exit()

def run():
    homepage()

