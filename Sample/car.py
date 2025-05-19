class Cars:

    def __init__(self,make,model,year,colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        
    def drive(self):
        print("this " +self.make+ " is driving")

Cars1 = Cars("toyota","camry",2025,"blue")
Cars2 = Cars("honda","civic",2010,"blue")

Cars1.drive()
Cars2.drive()
    
