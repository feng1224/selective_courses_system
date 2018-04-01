# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import accounts


class View(object):
    """ 视图父类 """

    account = accounts.Accounts()  # 关联Accounts对象，后续的登录，注册都需要使用
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None}

    def __init__(self):
        self.menu = None
        self.menu_dict = None
        self.result = None
        self.account_obj = None

    def login(self):
        """ 登录视图

        :return:
        """
        exit_flag = True
        while exit_flag:
            if not self.user_data['is_authenticated']:
                username = input('Please input username:').strip()
                password = input('Please input password:').strip()
                obj = self.account.getter(username, password)
                if obj:
                    print('\033[34;1mLogin Success！\033[0m')
                    self.user_data['account_id'] = obj.id
                    self.user_data['is_authenticated'] = True
                    self.user_data['account_data'] = obj
                    return self.user_data
                else:
                    print('\033[31;1mUsername or Password error！\033[0m')
                    return False
            else:
                return self.user_data

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
            if not username or not password:
                print('\033[31;1mError:Username or Password cannot be null!\033[0m')
                continue
            elif username == password:
                print('\033[31;1mError:Username Cannot be equal to Password !\033[0m')
                continue
            elif password != re_password:
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

    def tell_info(self):
        """ 展示账户信息方法
            本方法是一个视图，用来展示用户的个人信息。

        :return:
        """
        user_data_obj = self.user_data['account_data']
        user_info_data = user_data_obj.user_info
        print(user_info_data)
        # 通过反射，判断user_info_data对象中是否想相应的属性。如有就赋值。如没有设置为Null
        if hasattr(user_info_data, 'name'):
            name = getattr(user_info_data, 'name')
        else:
            name = 'Null'

        if hasattr(user_info_data, 'age'):
            age = getattr(user_info_data, 'age')
        else:
            age = 'Null'

        if hasattr(user_info_data, 'sex'):
            sex = getattr(user_info_data, 'sex')
        else:
            sex = 'Null'

        info = '''
==================账户信息==================
         ID：         \033[34;1m%s\033[0m
         Account：    \033[34;1m%s\033[0m
         Fullname：   \033[34;1m%s\033[0m
         Age：        \033[34;1m%s\033[0m
         Sex：        \033[34;1m%s\033[0m
         Type：       \033[34;1m%s\033[0m
         Status:      \033[34;1m%s\033[0m
============================================
        ''' % (user_data_obj.id, user_data_obj.username, name, age, sex, user_data_obj.account_type, user_data_obj.status)
        print(info)

    def set_info(self):
        """ 设置个人信息
        :return:
        """

        # 有个bug当设置用户详细信息时，可能会发生none的问题。现象重现：在学员界面，选择2，登录后在设置后会发生type和status = None
        exit_flag = True
        while exit_flag:
            fullname = input('Please input your fullname:').strip()
            sex = input('Please input your sex:').strip()
            age = input('Please input your age:').strip()

            obj = self.account.set_info(self.user_data['account_data'], fullname, sex, age)
            if obj:
                self.user_data['account_data'] = obj
                print('\033[34;1mSet Success！\033[0m')
                exit_flag = False

    def logout(self):
        self.user_data = {
            'account_id': None,
            'is_authenticated': False,
            'account_data': None}
        print('\033[34;1m Account logout!\033[0m')


class StudentView(View):
    """ 学生视图 """

    def __init__(self):
        super(StudentView, self).__init__()

    def choise_courses(self):
        """ 选课视图方法

        :return:
        """
        exit_flag = True
        while exit_flag:
            print('Input school and course. Input format like "beijing.python"')
            course = input('Please input your school and course():').strip()
            # obj = self.
            exit_flag = False

    def payment(self):
        """ 付款视图方法

        :return:
        """
        pass


class TeacherView(View):
    """ 老师视图 """

    def __init__(self):
        super(TeacherView, self).__init__()


class AdminView(View):
    """ 管理员视图 """

    account = accounts.Accounts()
    account.setter(username='admin', password='admin', account_type=0, status=0)
    def __init__(self):
        super(AdminView, self).__init__()


#     account = accounts.Accounts()  # 关联Accounts对象，后续的登录，注册都需要使用
#     def __init__(self):
#         self.menu = None
#         self.menu_dict = None
#         self.result = None
#         self.user_data = {
#             'account_id': None,
#             'is_authenticated': False,
#             'account_data': None}
#
#
#     def login(self):
#         """ 登录视图
#
#         :return:
#         """
#         exit_flag = True
#         while exit_flag:
#             if self.user_data['is_authenticated'] == False:
#                 username = input('Please input username:').strip()
#                 password = input('Please input password:').strip()
#                 obj = self.account.getter(username, password)
#                 if obj:
#                     print('\033[34;1mLogin Success！\033[0m')
#                     self.user_data['account_id'] = obj.id
#                     self.user_data['is_authenticated'] = True
#                     self.user_data['account_data'] = obj
#                     return self.user_data
#                 else:
#                     print('\033[31;1mUsername or Password error！\033[0m')
#                     return False
#             else:
#                 return self.user_data
#             exit_flag = False
#
#
#     def register(self):
#         """ 注册视图
#             支持注册后立即登录系统。
#         :return:
#         """
#         exit_flag = True
#         while exit_flag:
#             username = input('Please input username:').strip()
#             password = input('Please input password:').strip()
#             re_password = input('Please input password confirmation:').strip()
#             """下面代码，判断用户名是否等于密码。如果等于的话会报错。坦诚说,
#             是因为注册账号时的account_id是用用户名的MD5算出来的，如果密码和用户名一样，账号的ID就和密码的MD5一样.
#             所以添加这行代码,不让用户名和密码一样。其实也是一种伪装自己bug的方法（笑哭脸）。后续会改进"""
#             if not username or not password:
#                 print('\033[31;1mError:Username or Password cannot be null!\033[0m')
#                 continue
#             elif username == password:
#                 print('\033[31;1mError:Username Cannot be equal to Password !\033[0m')
#                 continue
#             elif password != re_password:
#                 print('\033[31;1mError:Password do not match!\033[0m')
#                 continue
#             else:
#                 type_id = 8
#                 status = 0
#                 # 注册新账号
#                 obj = self.account.setter(username, password, type_id, status)
#                 if obj:
#                     print('\033[34;1mRegistry Success！\033[0m')
#                     print('\033[34;1m"%s" account login！\033[0m' % username)
#                     self.user_data['account_id'] = obj.id
#                     self.user_data['is_authenticated'] = True
#                     self.user_data['account_data'] = obj
#                     exit_flag = False
#                 else:
#                     print('\033[31;1mThe user has already existed!\033[0m')
#                     continue
#
#     def tell_info(self):
#         """ 展示账户信息方法
#             本方法是一个视图，用来展示用户的个人信息。
#
#         :return:
#         """
#         user_data_obj = self.user_data['account_data']
#         user_info_data = user_data_obj.user_info
#         # 通过反射，判断user_info_data对象中是否想相应的属性。如有就赋值。如没有设置为Null
#         if hasattr(user_info_data, 'name'):
#             name = getattr(user_info_data, 'name')
#         else:
#             name = 'Null'
#
#         if hasattr(user_info_data,'age'):
#             age = getattr(user_info_data, 'age')
#         else:
#             age = 'Null'
#
#         if hasattr(user_info_data,'sex'):
#             sex = getattr(user_info_data, 'sex')
#         else:
#             sex = 'Null'
#
#         info = '''
# ==================账户信息==================
#          ID：         %s
#          Account：   %s
#          Fullname：   %s
#          Age：        %s
#          Sex：        %s
#          Type：       %s
#          Status:      %s
# ============================================
#         ''' %(user_data_obj.id, user_data_obj.username, name, age, sex,user_data_obj.type, user_data_obj.status)
#         print(info)
#
#     def set_info(self):
#         """ 设置个人信息
#
#         :return:
#         """
#         exit_flag = True
#         while exit_flag:
#             fullname = input('Please input your fullname:').strip()
#             sex = input('Please input your sex:').strip()
#             age = input('Please input your age:').strip()
#             obj = self.account.set_info(fullname, sex, age)
#             # print(obj.__dict__)
#             if obj:
#                 self.user_data['account_data'] = obj
#                 print('\033[34;1mSet Success！\033[0m')
#                 exit_flag = False
#
#     def logout(self):
#         self.user_data = {
#             'account_id': None,
#             'is_authenticated': False,
#             'account_data': None}
#         print('\033[34;1m Account logout!\033[0m')
# def Ilogin(obj):
#     EXIT_FLAG = True
#     while EXIT_FLAG:
#         result = obj.login()
#         EXIT_FLAG = False
#         return result
#
