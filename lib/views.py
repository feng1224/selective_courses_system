# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
import hashlib
from lib import accounts

class View(object):
    pass


class StudentView(View):

    def __init__(self):
        self.menu = None
        self.menu_dict = None
        self.result = None
        self.account = accounts.Accounts() # 关联Accounts对象，后续的登录，注册都需要使用
        self.user_data = {
            'account_id': None,
            'is_authenticated': False,
            'account_data': None}


    def login(self):
        """ 登录视图

        :return:
        """
        exit_flag = True
        while exit_flag:
            if self.user_data['is_authenticated'] == False:
                username = input('Please input username:').strip()
                password = input('Please input password:').strip()
                obj = self.account.getter(username, password)
                if obj:
                    print('\033[34;1mLogin Success！\033[0m')
                    self.user_data['account_id'] = obj.id
                    self.user_data['is_authenticated'] = True
                    self.user_data['account_data'] = obj
                else:
                    print('\033[31;1mUsername or Password error！\033[0m')
            else:
                print('haha')
            exit_flag = False


    def register(self):
        """ 注册视图
            支持注册后立即登录系统。
        :return:
        """
        exit_flag = True
        while exit_flag:
            username = input('Please input username:').strip()
            password = input('Please input password:').strip()
            re_password = input('Please input password confirmation:').strip()
            """下面代码，判断用户名是否等于密码。如果等于的话会报错。坦诚说,
            是因为注册账号时的account_id是用用户名的MD5算出来的，如果密码和用户名一样，账号的ID就和密码的MD5一样.
            所以添加这行代码,不让用户名和密码一样。其实也是一种伪装自己bug的方法（笑哭脸）。后续会改进"""
            if username == password:
                print('\033[31;1mError:Username Cannot be equal to Password !\033[0m')
                continue
            if password != re_password:
                print('\033[31;1mError:Password do not match!\033[0m')
                continue
            else:
                type_id = 8
                status = 0
                # 注册新账号
                obj = self.account.setter(username, password, type_id, status)
                if obj:
                    print('\033[34;1mRegistry Success！\033[0m')
                    print('\033[34;1m"%s" account login！\033[0m' % username)
                    self.user_data['account_id'] = obj.id
                    self.user_data['is_authenticated'] = True
                    self.user_data['account_data'] = obj
                    exit_flag = False
                else:
                    print('\033[31;1mThe user has already existed!\033[0m')
                    continue

    def tell(self):
        """ 展示账户信息

        :return:
        """
        user_data_obj = self.user_data['account_data']
        if hasattr(user_data_obj, 'name') or hasattr(user_data_obj,'age') or hasattr(user_data_obj,'sex'):
            name = user_data_obj.name
            age = user_data_obj.age
            sex = user_data_obj.sex
        else:
            name = None
            age = None
            sex = None
        print(user_data_obj.__dict__)
        info = '''
==================账户信息==================
         ID：         %s
         Username：   %s
         Fullname：   %s
         Age：        %s
         Sex：        %s
============================================
        ''' %(user_data_obj.id, user_data_obj.username, name, age, sex)
        print(info)





# class TeacherView(object):
#
#     def homepage(self):
#         pass
#
# class AdminView(object):
#     def homepage(self):
#         pass
#
# def Ilogin(obj):
#     EXIT_FLAG = True
#     while EXIT_FLAG:
#         result = obj.login()
#         EXIT_FLAG = False
#         return result
#







