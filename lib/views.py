# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib.accounts import *
from lib.schools import *
from lib.courses import *
from lib.classes import *
from lib.db import *


class View(object):
    """ 视图父类 """

    account = Accounts()  # 关联Accounts对象，后续的登录，注册都需要使用
    school = Schools()
    course = Courses()
    classes = Classes()
    account_storage = inter_db_handler(settings.ACCOUNT_DATABASE)
    base_storage = inter_db_handler(settings.BASE_DATABASE)
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None}
    # school_data = {'school': None,
    #                'course': [],
    #                'class': [],
    #                'teacher': [],
    #                'student': []}
    base_data = {'school': None,
                   'course': {},
                   'class': {},
                   'teacher': {},
                   'student': {}}

    def __init__(self):
        self.menu = None
        self.menu_dict = None
        self.result = None
        self.account_obj = None

    def login(self, account_type):
        """ 登录视图

        :return:
        """
        exit_flag = True
        while exit_flag:
            if not self.user_data['is_authenticated']:
                username = input('Please input username:').strip()
                password = input('Please input password:').strip()
                obj = self.account.getter(username, password)
                # print(obj.__dict__)
                # print(obj.account_type, account_type)
                if obj and obj.account_type == account_type:  # 判断账户的类型与账户是否存在
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

    def register(self, account_type, account_status):
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
                # 注册新账号
                obj = self.account.setter(username, password, account_type, account_status)
                if obj:
                    print('\033[34;1mRegistry Success！\033[0m')
                    print('\033[34;1m"%s" account login！\033[0m' % username)
                    self.user_data['account_id'] = obj.id
                    self.user_data['is_authenticated'] = True
                    self.user_data['account_data'] = obj
                    print(obj.__dict__)
                    exit_flag = False
                else:
                    print('\033[31;1mThe user has already existed!\033[0m')
                    continue

    def tell_info(self):
        """ 展示账户信息方法
            本方法是一个视图，用来展示用户的个人信息。

        :return:
        """
        # print(self.user_data)
        user_data_obj = self.user_data['account_data']
        user_info_data = user_data_obj.user_info
        # print(user_info_data)
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
        ''' % (user_data_obj.id, user_data_obj.username, name, age,
               sex, user_data_obj.account_type, user_data_obj.status)
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

    def change_password(self):
        # print(self.user_data['account_data'])
        exit_flag = True
        while exit_flag:
            old_password = input('Please input your old password:').strip()
            new_password = input('Please input your new password:').strip()
            re_new_password = input('Please input your new pasword confirmation:').strip()

            obj = self.account.getter(self.user_data['account_data'].username, old_password)
            # print(obj.__dict__)
            if obj:
                if not new_password or not re_new_password:
                    print('\033[31;1mError:Password cannot be null!\033[0m')
                elif new_password != re_new_password:
                    print('\033[31;1mError:Password do not match!\033[0m')
                else:
                    result = self.account.change_password(obj, new_password)
                    if result:
                        exit_flag = False
            else:
                print('\033[31;1mError: Password error!\033[0m')

    def logout(self):
        self.user_data = {
            'account_id': None,
            'is_authenticated': False,
            'account_data': None}
        print('\033[34;1m Account logout!\033[0m')
        print(self.user_data)


class StudentView(View):
    """ 学生视图 """
    account = StudentAccounts()
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None}

    def __init__(self):
        super(StudentView, self).__init__()

    def register(self, account_type, account_status):
        print('================创建学生=================')
        super(StudentView, self).register(account_type, account_status)

    def choise_courses(self):
        """ 选课视图方法

        :return:
        """
        print('================购买课程=================')
        exit_flag = True
        while exit_flag:
            print('Please Input school and course. Input format like "beijing.python"')
            course_seq = input('>>:').strip()
            if not course_seq:
                print('\033[031;1mError: Input cannot be null!\033[0m')
            elif not '.' in course_seq:
                print('\033[031;1mError: Input format error!\033[0m')
            else:
                school_name, course_name = course_seq.split('.')
                print(school_name, course_name)
                school_result = self.school.getter(school_name)

                # # if school_result:
                # #     for course_obj in school_result['course']:
                # #         if course_obj.name == course_name:
                # #             if self.payment(course_obj.price):
                # #                 obj = self.account.set_student_data(self.user_data['account_data'], )
                # #                 if obj:
                # #                     self.user_data['account_data'] = obj
                # #                     print('\033[34;1mSet Success！\033[0m')
                # #                     exit_flag = False
                #
                #
                #         else:
                #             print('\033[031;1mError: The course does not exist!\033[0m')
                # else:
                #     print('\033[031;1mError: The school does not exist!\033[0m')
            # obj = self.
            exit_flag = False

    def payment(self, pay):
        """ 付款视图方法
        该方法是一个假方法，并没有任何账号支付的动作。
        只是比较一下用户输入的价格是否和课程的价格一致。
        :return:
        """
        exit_flag = True
        while exit_flag:
            tuition = input('Please pay tuition [%s RMB]：' % pay).strip()
            if not tuition:
                print('\033[031;1mError:Tuition cannot be null!\033[0m')
            else:
                if tuition == pay:
                    return True
                else:
                    return False


class TeacherView(View):
    """ 老师视图 """
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None}

    def __init__(self):
        super(TeacherView, self).__init__()


class AdminView(View):
    """ 管理员视图 """

    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None}
    account = Accounts()
    account.setter(username=settings.DEFAULT_ADMIN_ACCOUNT,
                   password=settings.DEFAULT_ADMIN_PASSWORD, account_type=1, status=0)

    def __init__(self):
        super(AdminView, self).__init__()

    def create_school(self):
        """ 管理员创建学校视图方法

        :return:
        """
        exit_flag = True
        while exit_flag:
            print('================创建学校=================')
            name = input('Please input name of school:').strip()
            city = input('Please input city of school:').strip()
            location = input('Please input address of school:').strip()
            if not name or not city:
                print('\033[031;1m Error: Cannot be null!')
            else:
                obj = self.school.setter(name, city, location)
                if obj:
                    self.base_data['school'] = obj
                    self.base_storage.nonquary(name, self.base_data)
                    print('\033[034;1mCreate school success!\033[0m')
                    exit_flag = False
                else:
                    print('\033[031;1mSchool has already existed!\033[0m')
                    exit_flag = False

    def create_courses(self):
        """ 管理员创建课程视图方法

        :return:
        """
        print('================创建课程=================')
        exit_flag = True
        while exit_flag:
            course_name = input('Please input course name:')
            price = input('Please input price:')
            period = input('Please input term:')
            school_name = input('Please input associated school:')
            school_result = self.school.getter(school_name)
            if not course_name or not price or not period or not school_name:
                print('\033[031;1m Cannot be null!\033[0m')
            elif not price.isdigit() or not period.isdigit():
                print('\033[031;1m Price and Period must be integer!\033[0m')
            elif not school_result:
                print('\033[031;1mSchool does not exist\033[0m')
            elif course_name in school_result['course']:
                print('\033[031;1mCourse has already existed!\033[0m')
            else:
                # print(school_result)
                obj = self.course.setter(course_name, int(price), int(period))
                if obj:
                    school_result['course'][course_name] = obj
                    print(school_result)
                    self.base_storage.nonquary(school_name, school_result)
                    print('\033[034;1mCreate course success!\033[0m')
                    exit_flag = False
                else:
                    print('\033[031;1mCreate course failed!\033[0m')
                    exit_flag = False
                # print(school_result)
                # if school_result['course'] == []:
                #     obj = self.course.setter(course_name, int(price), int(period))
                #     school_result['course'].append(obj)
                #     self.school.set_info(school_name, school_result)
                #     print('\033[034;1mCreate course success!\033[0m')
                #     exit_flag = False
                # else:
                #     course_name_list = []
                #     for course_obj in school_result['course']:
                #         course_name_list.append(course_obj.name)
                #     if course_name in course_name_list:
                #         print('\033[031;1mCourse has already existed!\033[0m')
                #         exit_flag = False
                #     else:
                #         obj = self.course.setter(course_name, int(price), int(period))
                #         school_result['course'].append(obj)
                #         self.school.set_info(school_name, school_result)
                #         print('\033[034;1mCreate course success!\033[0m')
                #         exit_flag = False

    def create_classes(self):
        """ 创建班级视图方法

        :return:
        """
        print('================创建班级=================')
        exit_flag = True
        while exit_flag:
            class_name = input('Please input class name:').strip()
            course = input('Please input associated course:').strip()
            teacher = input('Please input associated teacher:').strip()
            school_name = input('Please input associated school:').strip()
            school_result = self.school.getter(school_name)
            # print(school_result)
            course_list = school_result['course']
            teacher_list = school_result['teacher']
            if not course or not class_name or not course or not teacher or not school_name:
                print('\033[031;1m Cannot be null!\033[0m')
            if not school_result:
                print('\033[031;1m School designation error!\033[0m')
                exit_flag = False

            course_result = None
            for course_obj in course_list:
                if course_obj.name == course:
                    course_result = course_obj
                else:
                    course_result = None

            teacher_result = None
            for teacher_obj in teacher_list:
                # print(teacher_obj.__dict__)
                if teacher_obj.username == teacher:
                    teacher_result = teacher_obj
                else:
                    teacher_result = None

            if not course_result or not teacher_result:
                print('\033[031;1mError: Course or Teacher designation error!\033[0m')
                exit_flag = False
            else:
                obj = self.classes.setter(class_name, course_result, teacher_result)
                if obj:
                    school_result['class'].append(obj)
                    print(school_result)
                    self.school.set_info(school_name, school_result)
                    print('\033[034;1mCreate class success！\033[0m')
                    exit_flag = False
                else:
                    print('\033[031;1mError: Create class failed!\033[0m')

    def create_teachers(self, account_type, account_status):
        """ 创建老师视图方法

        :param account_type:
        :param account_status:
        :return:
        """
        print('================创建老师=================')
        exit_flag = True
        while exit_flag:
            username = input('Please input username:').strip()
            password = input('Please input password:').strip()
            re_password = input('Please input password confirmation:').strip()
            school_name = input('Please input associated school:').strip()
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
                school_result = self.school.getter(school_name)
                if school_result:
                    # 注册新账号
                    obj = self.account.setter(username, password, account_type, account_status)
                    if obj:
                        school_result['teacher'].append(obj)
                        self.school.set_info(school_name, school_result)
                        print('\033[34;1mRegistry Success！\033[0m')
                        exit_flag = False
                    else:
                        print('\033[31;1mThe user has already existed!\033[0m')
                        continue
                else:
                    print('\033[031;1m School designation error!\033[0m')
