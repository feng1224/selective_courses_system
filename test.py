# -*-coding: utf-8 -*-
import pickle
class Teacher:
    def __init__(self, name, age, sex, salary, course_name, course_period, course_price):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.course = Course(course_name,course_period,course_price)  # 组合Course类

    def teach(self):
        print('Teaching!')


class Course:
    def __init__(self, course_name, course_period, course_price):
        self.course_name = course_name
        self.course_period = course_period
        self.course_price = course_price

    def tell_info(self):
        info = """-------COURSE INFO--------
        Course = %s
        Period = %s
        Price = %s
        """ % (self.course_name, self.course_period, self.course_price)
        print(info)


teacher1 = Teacher('henry', 29, 'man', 1000, 'Python', 1, 20)
print(teacher1.__dict__)  # 打印teacher1对象的属性
print('teacher1 teach %s' % teacher1.course.course_name)  # 打印teacher1对象组合后的来的course属性的course_name属性
teacher1.course.tell_info()

f = open('test','wb')
pickle.dump(teacher1,f,0)