# -*-coding: utf-8 -*-
# Auther： Henry Yuan

class Accounts(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.type = None
        self.status = None
        self.user_info = None

    def getter(self):
        """ 获取账号

        :return:
        """
        result = {'username': self.username,
                  'password': self.password,
                  'type': self.type,
                  'status': self.status,
                  'user_info': self.user_info}
        return result

    def setter(self, username, password, type, status):
        """ 创建账号

        :return:
        """
        self.username = username
        self.password = password
        self.type = type
        self.status = status



    def create_id(self):
        """ 创建账号的ID

        :return:
        """

    def __check(self):
        pass
class Admin(Accounts):

    def __init__(self,username, password, type, status):
        super(Admin, self).__init__(username, password, type, status)