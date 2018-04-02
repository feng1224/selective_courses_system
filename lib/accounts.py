# -*-coding: utf-8 -*-
# Auther： Henry Yuan
from lib import db
from conf import settings
import hashlib
import os
from lib import persion


class Accounts(object):
    """ 账号父类 """
    storage = db.inter_db_handler(settings.ACCOUNT_DATABASE)
    human = persion.Teacher()

    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        self.account_type = None
        self.status = None
        self.user_info = None

    def getter(self, username, password):
        """ 获取账号

        :return:
        """
        self.id = self.create_hash(username)
        self.username = username
        self.password = self.create_hash(password)
        # print(self.username, self.password)
        if self.__check_username():
            return False

        else:
            result = self.storage.quary(self.id)
            # print(result)
            if self.password == result.password:
                # print(result.__dict__)
                return result
            else:
                return False

    def setter(self, username, password, account_type, status):
        """ 创建账号
            对应View类的register方法。用以注册、创建账号时使用

        :return:
        """
        self.id = self.create_hash(username)
        self.username = username
        self.password = self.create_hash(password)
        self.account_type = account_type
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
        """ 封装方法-检查账号的用户名是否存在数据库

        :param username:
        :return:
        """
        if not os.path.exists('%s/%s' % (self.storage.db_path,self.id)):
            return True
        else:
            return False

    def set_info(self, account_data, name, sex, age):
        """ 设置账号的基本信息

        :param account_data:  用户登录后的账号数据
        :param name: 用户的真实姓名
        :param sex:  用户的性别
        :param age:  用户的年龄
        :return:
        """
        self.human.name = name
        self.human.sex = sex
        self.human.age = age
        account_data.user_info = self.human
        self.storage.nonquary(self.id, account_data)
        return account_data

    def change_password(self, account_data, new_password):
        self.new_password = self.create_hash(new_password)
        account_data.password = self.new_password
        print(account_data.__dict__)
        self.storage.nonquary(self.id, account_data)
        return account_data


class StudentAccounts(Accounts):

    def __init__(self):
        pass


class AdminAccounts(Accounts):

    storage = db.inter_db_handler(settings.ADMIN_ACCOUNT_DATABASE)

    def __init__(self):
        super(AdminAccounts, self).__init__()

    def getter(self, username, password):
        """ 获取管理员账号

        :param username:
        :param password:
        :return:
        """
        result = super(AdminAccounts, self).getter(username, password)
        if result:
            return result
        else:
            return False


    def setter(self, username=settings.DEFAULT_ADMIN_ACCOUNT, password=settings.DEFAULT_ADMIN_PASSWORD, account_type=0, status=0):
        """ 创建管理员账号

        :return:
        """
        # print(username, password)
        super(AdminAccounts, self).setter(username, password, account_type, status)

    def __check_username(self):
        """ 检查账号的用户名是否存在数据库

        :param username:
        :return:
        """
        if not os.path.exists('%s/%s' % (self.storage.db_path, self.id)):
            return True
        else:
            return False


if __name__ == '__main__':
    import pickle
    ac = Accounts()
    ac.setter('1234','12345',1,2)

    print(ac.__dict__)
    ac.set_info('1234','12345',19)
    print(ac.__dict__)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(base_dir)
    with open('%s/db/accounts/%s'% (base_dir,ac.id)) as f:
        print(pickle.load(f.encoding('utf-8')))
