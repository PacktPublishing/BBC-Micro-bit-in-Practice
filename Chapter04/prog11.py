class fruit:
    
    def __init__(self, str):
        self.name = str
    
    def printName(self):
        print(self.name)


f1 = fruit('Mango')
print(type(f1))
f1.printName()
