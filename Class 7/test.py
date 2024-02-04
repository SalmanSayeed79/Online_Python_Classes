class Person:
    # Consturctor
    def __init__(self,name,age,height,mass):
        self.name=name
        self.age=age
        self.height=height
        self.mass=mass
                
    def show(self):
        print("This person is ",self.name," his age is ",self.age)
            
    def calculateBMI(self):
        return self.mass/self.height**2
    
    
        
# Class vs Object 
sakib=Person("sakib",25,1.76,70)
rahim=Person("rahim",32,1.56,90)

karim=Person("karim",-1,-1,-1)

