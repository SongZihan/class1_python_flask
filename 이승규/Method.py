class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def Area(self): # 인스턴스 메소드
        area = self.width * self.height
        return area

    def Count(self): # 클래스 메소드
        print(self.count)

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 2)
rect1.Count() # 2 출력
print(Rectangle.count) # 2 출력
print("{}*{}={}".format(rect1.width, rect1.height, rect1.Area())) # 3*4=12 출력
print("{}*{}={}".format(rect2.width, rect2.height, rect2.Area())) # 5*2=10 출력