# 1. What is Class? / How to use class(basic)?
#    Class is sum of functions and variables
#    For using class, we have to make and def it first

class introduce:
    name = "Python"
    age = "28"
    def info(self):
        print('나는', self.name, '입니다. 그리고', self.age, '살 입니다.')

print(type(introduce))
print(introduce)

# 2. What is constructor？
#    consturctor initiallizes and recalls instances

class introduce:
    name = "Python" # class variables
    age = 28        # class variables
    def __init__(self, name, age): # __init__ is class's constructor
        self.name = name # instance variables
        self.age = age   # instance variables
    def intro(self):
        print('나는 ' + self.name + '입니다. 그리고 ' + self.age + '살 입니다.')
        print('잘 부탁드립니다!')

Py=introduce('Python', '28')
Py.intro()