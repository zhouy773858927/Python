class Property:#属性类
    def __init__(self):
        self.high = 0
        self.width = 0
    def setSize(self,size):
        self.high,self.width = size
    def getSize(self):
        return self.high,self.width

p=Property()
p.high = 10
p.width = 5
print(p.getSize())

p.setSize((150,100))#setSize(self,size);(150,100) == size
print(p.high)