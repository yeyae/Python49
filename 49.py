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
    def add(self):
