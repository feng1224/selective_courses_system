# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import abc
import pickle
import os


class Database(object, metaclass=abc.ABCMeta):
    """Database抽象类
        对所有以后可能扩展的数据库类的子类进行归一化
    """
    def __init__(self, conn_params, username, password):
        self.conn_params = conn_params
        self.username = username
        self.password = password
        self.db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    @abc.abstractmethod
    def connect(self):
        """ 连接数据库方法
        """
        pass

    @abc.abstractmethod
    def close(self):
        """ 关闭数据库方法
        """
        pass


class FileStorage(Database):
    """文件存储类"""

    def __init__(self, conn_params, username, password):
        super(FileStorage, self).__init__(conn_params, username, password)

    def connect(self):
        """ 数据库连接方法
            但由于FileStorage类是使用文件进行存储。不需要先连接数据库。
            所以connect在FileStorage类中，主要是检查self.db_path的路径是否存在。
        :return:
        """
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)

    def load_data(self, file):
        """
        读取数据到内存中
        :param file: 读取的文件名
        :return: 返回信息
        """
        with open('%s/%s' % (self.db_path, file), "rb") as f:
            data = pickle.load(f)
            return data

    def dump_data(self, file, data):
        """
        从内存中把数据写入到数据库中
        :param file: 写入的文件名
        :param data: 保存的数据
        :return:
        """
        with open('%s/%s' % (self.db_path, file), 'wb') as f:
            pickle.dump(data, f)
        return True

    def close(self):
        pass


class MysqlStroage(Database):
    """Mysql存储类
        扩展功能
    """
    def __init__(self, conn_params, username, password):
        super(MysqlStroage, self).__init__(conn_params, username, password)

    def connect(self):
        pass

    def close(self):
        pass


def inter_db_handler(conn_params):
    """db_handler接口

        为File_storage类、Mysql_storage类定义一个接口。创建对象时可以通过这个接口创建。

    :param conn_params: 数据库连接参数
    :return:
    """
    if conn_params['engine'] == 'file_storage':
        file_db = FileStorage(conn_params, conn_params['username'], conn_params['password'])
        return file_db

    # 扩展功能，支持mysql存储
    elif conn_params['engine'] == 'mysql_storage':
        mysql_db = MysqlStroage(conn_params, conn_params['username'], conn_params['password'])
        return mysql_db


def inter_db_connect(obj):
    """ connect接口

    所有的数据库连接使用该接口。
    :param obj:
    :return:
    """
    obj.connect()


def inter_file_load_data(obj, file):
    obj.load_data(file)


def inter_file_dump_data(obj, file, data):
    obj.dump_data(file, data)


# 模块调试（开源后需删除）
if __name__ == '__main__':
    from conf import settings
    db = inter_db_handler(settings.ACCOUNT_DATABASE)
    print(db)
    print(db.__dict__)
    inter_db_connect(db)
    db.dump_data('test',{'name':1},)
    db = inter_db_handler(settings.BASE_DATABASE)
    print(db)
    print(db.__dict__)
