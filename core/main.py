# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
from . import operators
from lib import views
from lib import accounts

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

account = accounts.Accounts()
student_views = views.StudentView()
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
            eval(menu_dict[cmd])
        else:
            print('选项不存在')

def homepage():
    menu = '''
    1. 学生登录通道
    2. 教师登录通道
    3. 管理员登录通道
    4. 退出
    '''
    menu_dict = {'1': 'student_homepage()',
                 '2': 'views.TeacherView()',
                 '3': 'views.AdminView()',
                 '4': 'logout()'}
    result = interactive(menu, menu_dict)
    return result

def student_homepage():

    menu = '''
    ===============欢迎进入学员视图===============
                      1. 注册
                      2. 账户信息
                      3. 选择课程
    ==============================================
    '''
    menu_dict = {
                 '1': 'register()',
                 '2': 'infomation()',
                 '3': 'choise()'}
    interactive(menu, menu_dict)

def login(func):
    def inner():
        # exit_flag = True
        # while exit_flag:
        #     if user_data['is_authenticated'] == False:
        #         result = student_views.login()
        #         if result:
        #             print('\033[34;1mLogin Success！\033[0m')
        #             user_data['account_id'] = result.id
        #             user_data['is_authenticated'] = True
        #             user_data['account_data'] = result
        #             exit_flag = False
        #             func()
        #         else:
        #             print('\031[34;1mUsername or Password error！\033[0m')
        #     else:
        #         exit_flag = False
        #         func()
        student_views.login()
        func()
    return inner

def register():
    student_views.register()



@login
def infomation():
    student_views.tell()
    #print(obj.__dict__)

def logout():
    sys.exit()

def run():
    homepage()

