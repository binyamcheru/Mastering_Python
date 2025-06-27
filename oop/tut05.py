## Encapsulation 
class PersonPublic:
    def __init__(self,name,age):
        self.name = name # public variable
        self.age = age   # public variable

person1 = PersonPublic("John",23)
print(person1.name)

# private variables = just include double underscore __var
class PersonPrivate:
    def __init__(self,name,age,gender):
        self.__name = name # private variable
        self.__age = age   # private variable
        self.gender = gender   # public variable

person2 = PersonPrivate("John",23,"Male")
print(person2)
# print(person1.name) # Error

# protected variables = just include single underscore _var
class PersonProtected:
    def __init__(self,name,age,gender):
        self._name = name # protected variable
        self._age = age   # protected variable
        self.gender = gender   # public variable


class Employee(PersonProtected):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

employee = Employee("Jonathan",23,"Male")
print(employee._name)

# Getter and Setter
class Person:
    def __init__(self,name,age):
        self.__name = name 
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age can't be negative")

print()
print()
person = Person("Peter",23)
print(person.get_name())
print(person.get_age())

person.set_age(34)
print(person.get_age())

person.set_age(-2)