import pickle

class Foo:
    def __init__(self,name):
        self.name = name

    def fuck(self):
        print('haha')

f2 = Foo('fuck')
with open('test','ab') as f:
    pickle.dump(f2,f)

with open('test','rb') as f:
    test = pickle.load(f)

print(test.__dict__)