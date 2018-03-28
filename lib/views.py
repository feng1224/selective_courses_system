# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
import hashlib
from lib import accounts


class StudentView(object):

    def __init__(self):
        self.menu = None
        self.menu_dict = None
        self.account = accounts.Accounts()  # 关联Accounts对象，后续的登录，注册都需要使用

    @property
    def homepage(self):
        self.menu = '''
        ===============欢迎进入学员视图===============
                          1. 登录
                          2. 注册
                          3. 选择课程
        ==============================================
        '''
        self.menu_dict = {'1': 'self.login()',
                          '2': 'self.register()',
                          '3': 'self.choise()'}
        Flag = True
        while Flag:
            print(self.menu)
            cmd = input('>>:').strip()
            if cmd in self.menu_dict:
                eval(self.menu_dict[cmd])
            else:
                print('选项不存在')


    def register(self):
        Flag = True
        while Flag:
            username = input('Please input username:').strip()
            password = input('Please input password:').strip()
            re_password = input('Please input password confirmation:').strip()
            if password != re_password:
                print('\033[31;1mPasswords do not match!\033[0m')
            else:
                type = 8
                status = 0
                # 注册新账号
                self.account.setter(username, password, type, status)
                # 修改调试模式使用assert
                # assert isinstance("")
                print(self.account.__dict__)
                print('\033[34;1mRegistry Success！\033[0m')
                Flag = False

    def login(self):
        Flag = True
        while Flag:
            user_name = input('Please input username:').strip()
            password = input('Please input password:').strip()
            print(self.account.getter())
            if user_name in self.account.getter():
                print('\033[31;1mPasswords do not match!\033[0m')
            else:
                type = 'student'
                status = 0
                new_account = accounts.Accounts()
                print(new_account.__dict__)
                print('\033[34;1mLogin Success！\033[0m')
                Flag = False

class TeacherView(object):

    def homepage(self):
        pass

class AdminView(object):
    def homepage(self):
        pass