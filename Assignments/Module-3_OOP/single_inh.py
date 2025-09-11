class father:
    bal:int
    car:int
    
    def getdata(self):
        self.bal=input("Enter bank balance details:")
        self.car=input("Enter a car details:")

class son(father):
    def printdata(self):
        print("Balance:",self.bal)
        print("Car:",self.car)

sn=son()
sn.getdata()
sn.printdata()
        
    