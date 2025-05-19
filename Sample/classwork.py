class drugs:
    def __init__(self,type,expirydate,product):
           self.type = type
           self.expirydate = expirydate
           self.product = product

    def use(self):
        print("this " +self.type+ "")

