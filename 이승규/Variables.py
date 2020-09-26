class Values:
    value1 = 10 # 클래스 변수
    def __init__(self, value1):
        self.value1 = value1 # self. : 인스턴스 변수

    def __str__(self):
        return "{}".format(self.value1)

a = Values(100)
b = Values(300)

print("a : {}".format(a)) # "a : 100" 출력
print("b : {}".format(b)) # "b : 300" 출력
print(Values.value1) # "10" 출력

if __name__ == '__main__':
    #class variables
    print( 'Class variables is {}'.format(Values.value1))
    # instance variables
    values_instance = Values(20)
    print('Class variables is {}'.format(Values.value1))
    print('Instance variables is {}'.format(values_instance.value1))