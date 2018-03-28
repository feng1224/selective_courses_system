# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import schools
from lib import accounts
def login(func):
    def inner():
        print('login')
        func()
    return inner

def create_school():
    Flag = True
    while Flag:
        name = input('学校名称：').strip()
        city = input('城市：').strip()
        location = input('地址：').strip()
        if name or city or location:
            school = schools.Schools()
            result = school.setter(name, city, location)
            if result:
                print('新学校已创建:',school.getter())
            else:
                print('已有重名的学校')
            #Flag = False

def registry():
    Flag = True
    while Flag:
        user_name = input('Please input username:').strip()
        password = input('Please input password:').strip()
        re_password = input ('Please input password confirmation:').strip()
        if password != re_password:
            print('\033[31;1mPasswords do not match!\033[0m')
        else:
            type = 'student'
            status = 0
            new_account = accounts.Accounts(user_name,password,type,status)
            print(new_account.__dict__)
            print('\033[34;1mRegistry Success！')