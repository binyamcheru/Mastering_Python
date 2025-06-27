## Magic methods
## "__init__","__str__","__repr__","__len__"
# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# person = Person("John",25)
# print(person) # Output: <__main__.Person object at 0x000001D9090A6A50>

 
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age} years old"
    
    def __repr__(self):
        return f"Person(name:{self.name},age:{self.age})"

person = Person("John",25)
print(person) # Output: John,25 years old
print(repr(person))