# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import pickle

class Teacher(object):
    pass

class Course:
    pass

f = open('test','rb')
test = pickle.load(f)
print(test.name)
