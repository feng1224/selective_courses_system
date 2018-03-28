# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import accounts
class People(object):

    def __init__(self, name, sex, age, accounts):
        self.name = name
        self.sex = sex
        self.age = age
        self.account = accounts

    def getter(self):
        pass

    def setter(self, username, password, status, type):
        """ 注册账号

        :return:
        """
        user_name = input("Please input user name >>: ").strip()
        password = input("Please input password >>: ").strip()
        re_password = input("Please input password confirmation >>: ").strip()
        if password != re_password:
            print("\033[31;1mPasswords do not match!\033[0m")
            return False
        status = 1
        account = accounts.Accounts(user_name, password, status, type)
        new_account = account.create()
        self.account = new_account
        return self

    def login(self, accounts):
        pass

    def logout(self):
class Teacher(People):

    def __init__(self, name, sex, age):
        super(Teacher, self).__init__(name, sex, age)


class Student(People):

    def __init__(self, name, sex, age):
        super(Student, self).__init__(name, sex, age)

    def register(self):

