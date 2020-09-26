# What is class? How to use class(basic)?



# What is constructor？



class Student():

    is_human = True # 클래스 변수
    can_eat = True

    def __init__(self, age, name):
        # __init__ is python class's constructor.
        self.age = age # 인스턴스 변수
        self.name = name
        # do something
        print('This class is instantiated')


    def say_hello(self):
        """
        instance method
        인스턴스 메서드 사용은 먼저 클래스를 인스턴스화해야 합니다.인스턴스 메서드는 인스턴스 변수에 액세스하는 데 사용됩니다.
        """
        print('Hello I am ' + self.name)

    @classmethod # classmethod is a Decorator 다음 메소드가 클래스 메소드임을 나타냅니다.
    def student_is_human(cls):
        """
        클래스 메서드는 클래스 변수에 액세스하는 데 사용됩니다.
        :return:
        """
        return cls.is_human

    @staticmethod
    def walk():
        """
        정적 메서드(staticmethod)과 일반 함수에는 차이가 없습니다.분류를 위해 class에 배치 할 수 있습니다.
        """
        print('student can walk')



# The difference between class variables and instance variables.
"""
클래스 변수는 클래스의 고유 속성을 나타냅니다. 예를 들어, 학생들은 먹을 수 있습니다.
Student.is_human == True

인스턴스 변수는 클래스가 인스턴스화 된 후에만 소유 할 수있는 속성을 나타냅니다. 예 :
Xiao Ming은 학생이며 24 세입니다.
xiaoming = Student(24,'xiaoming') 
xiaoming.age == 24

그러나 학생들이 24 세라고 말하는 것은 잘못된 것입니다.
Student.age 없다.
"""

# The difference between class method and instance method.
"""
클래스 메서드는 클래스 변수에 액세스하는 데 사용됩니다.
인스턴스 메서드 사용은 먼저 클래스를 인스턴스화해야 합니다.인스턴스 메서드는 인스턴스 변수에 액세스하는 데 사용됩니다.
"""