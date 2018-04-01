class test(object):

    def __init__(self):
        self.__name = None
        self.__age = None

    @property
    def set(self):
        return self.__name, self.__age

    @set.setter
    def set(self, kwargs):
        print(kwargs)
        self.__name = kwargs['name']
        self.__age = kwargs['age']

if __name__ == '__main__':
    test1 = test()
    #print(test1.__dict__)
    test1.set = {'name': 'jem', 'age': 19}
    #print(test1.__dict__)
    print(test1.set)