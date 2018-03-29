# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import db
from conf import settings
import hashlib
import os


class Accounts(object):
    storage = db.inter_db_handler(settings.ACCOUNT_DATABASE)

    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        self.type = None
        self.status = None
        self.user_info = None

    def getter(self, username, password):
        """ 获取账号

        :return:
        """
        self.id = self.create_hash(username)
        self.username = username
        self.password = self.create_hash(password)
        if self.__check_username():
            return False

        else:
            result = self.storage.quary(self.id)
            if self.password == result.password:
                return result
            else:
                return False


    def setter(self, username, password, type, status):
        """ 创建账号
            对应View类的register方法。用以注册、创建账号时使用

        :return:
        """
        self.id = self.create_hash(username)
        self.username = username
        self.password = self.create_hash(password)
        self.type = type
        self.status = status
        if self.__check_username():
            self.storage.nonquary(self.id, self)  # 存储到数据库
            return self
        else:
            return False

    @staticmethod
    def create_hash(arg):
        """ hash创建方法
            使用用户名进行MD5校验计算出账号的ID和密码。
        :return:
        """
        md5_id = hashlib.md5()
        md5_id.update(arg.encode('utf-8'))
        return md5_id.hexdigest()

    def __check_username(self):
        """ 检查账号的用户名是否存在数据库

        :param username:
        :return:
        """
        if not os.path.exists('%s/%s' % (self.storage.db_path,self.id)):
            return True
        else:
            return False

    def show_info(self):
        pass

# class Admin(Accounts):
#
#     def __init__(self,username, password, type, status):
#         super(Admin, self).__init__(username, password, type, status)
#
if __name__ == '__main__':
    ac = Accounts()
    #ac.setter('henry','henry',1,2)
    print(ac.getter('henry','henry'))
    print(ac.__dict__)
