class FourCal:
    def __init__(self, first , second):
        self.first = first 
        self.second = second
    def setdata(self, frist, second):
        self.first = frist
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
        
a = FourCal(1,2)
a.setdata(4,2)
print(a.add())
