class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!!!")


dog1 = Dog("Buddy",2)
dog1.bark()

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited. New balance is {self.balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient funds.")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New balance is {self.balance}.")
    
    def get_balance(self):
        return self.balance
    

account = BankAccount("John",4000)
print(account.get_balance())
account.deposit(1220)
account.withdraw(1000)
print(account.get_balance())
