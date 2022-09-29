class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result        
#더하기 기능 만들기
a = FourCal()
a.setdata(4, 2)
print(a.add())

#곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def mul(self):
        result = self.first * self.second
        return result      

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sub(self):
        result = self.first - self.second
        return result      

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def div(self):
        result = self.first / self.second
        return result      

    def __init__(self, first, second):
        self.first = first
        self.second = second

a = FourCal(4,2)
print(a.first)
print(a.second)
a.add()
a.div()
a.sub()
a.mul()
