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
 result = self.first * self.second
        return result        
 result = self.first - self.second
        return result        
 result = self.first / self.second
        return result        

#기능들 결과 뽑아내기
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
