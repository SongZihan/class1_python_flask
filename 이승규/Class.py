class SGClass: # 클래스
    var = "I'm Lee SG." # 클래스 멤버
    def myName(self): # 클래스 메소드(첫번째 인자 = self)
        print(self.var)

obj = SGClass() # SGClass 인스턴스 객체 생성
print(obj.var) # "I'm Lee SG." 출력
obj.myName() # "I'm Lee SG." 출력
