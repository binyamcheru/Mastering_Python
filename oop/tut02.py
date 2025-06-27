# Single Inheritance
class Car:
    def __init__(self,windows,doors,engineType):
        self.windows = windows
        self.doors = doors
        self.engineType = engineType
    
    def drive(self):
        print(f"The person will drive the {self.engineType}.")

car1 = Car(4,5,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self, windows, doors, engineType,isSelfDriving):
        super().__init__(windows, doors, engineType)
        self.isSelfDriving = isSelfDriving

    def selfDriving(self):
        print(f"Tesla supports self driving: {self.isSelfDriving}")

tesla1 = Tesla(3,5,"electric",True)
tesla1.drive()
tesla1.selfDriving()

## MULTIPLE INHERITANCE

class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print("Subclass must implement this method.")
    
class Pet: 
    def __init__(self,owner):
        self.owner = owner

class Dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} says woof."

dog = Dog("Buddy","john")
print(dog.speak())
print(f"Owner: {dog.owner}")