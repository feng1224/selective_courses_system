class Accounts(object):
    """ 账号父类 """

    def __init__(self, username, password):
        self.username = username
        self.__password = self.generate_md5(self.check_password(password))

    @property
    def password(self):
        return self.__password

    def set_password(self, value):
        print(value)
        print(self.generate_md5(value))
        self.__password = self.generate_md5(value)

    @staticmethod
    def check_password(value):
        return value

    @staticmethod
    def generate_md5(value):
        return value + '123'

if __name__ == '__main__':
    test = Accounts('henry', '123')
    print(test.__dict__)
