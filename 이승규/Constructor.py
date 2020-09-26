import math

class Circle:
    def __init__(self, radius): # 생성자
        self.radius = radius

    def Length(self):
        return 2*self.radius*math.pi

    def Area(self):
        return (self.radius**2)*math.pi

c1 = Circle(3)
print("c1's radius : " + str(c1.radius)) # "c1's radius : 3" 출력
print("c1's length : " + str(round(c1.Length(),1))) # "c1's length : 18.8" 출력
print("c1's area : " + str(round(c1.Area(),1))) # "c1's area : 28.3" 출력

