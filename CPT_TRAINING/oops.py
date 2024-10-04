
#Oops
"""
class Car:
    name="Audi"
    colour="Black"
#object
car1=Car()
print(car1.colour)
print(car1.name)
"""
#output
"""
Black
Audi"""


#Construtur - Assigning values
"""
class Car:   #class Attribute
    
    car_type = "sedan"
    
    def __init__(self,name,milage):
        self.name=name
        self.milage=milage
        
    def description(self):
        return f"The {self.name} car gves milage of {self.milage}Km/1"
    
    def max_speed(self,speed):
        return f"The {self.name} runs at maximum speed of {speed} km/hr"

    def colour(self,c1):
        return f"The {self.name} car is in {c1} colour"
    
#object
obj=Car("Mustang",7)
print(obj.description())
print(obj.max_speed(150))
print(obj.colour("black"))
"""
#output:
"""
The Mustang car gves milage of 7Km/1
The Mustang runs at maximum speed of 150 km/hr
The Mustang car is in black colour"""


#Area of Rectangle
"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return f'area of rectangle is {self.length*self.width}'
    def perimeter(self):
        return f'perimeter of rectangle is {2*(self.length+self.width)}'
    def is_square(self):
        return self.length==self.width
obj=Rectangle(1,7)
print(obj.area())
print(obj.perimeter())
print(obj.is_square())"""

#Output1:
"""
area of rectangle is 16
perimeter of rectangle is 16
True

#output2:
area of rectangle is 7
perimeter of rectangle is 16
False"""

#Bank Account Management System
"""
class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        #return f'Today you deposited {amount} and your previous balance is {self.balance} and now your total balance is{self.balance+amount}'
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Funds")
            
    def display_balance(self):
        print(f"Balance for {self.name}:${self.balance:.2f}")
        #return f'your withdrawl is {amount} and updated bank balance is {self.balance-amount}'
        
obj=bank_account("dharan",10000)
obj.display_balance()
obj.deposit(10000.0)
obj.display_balance()
obj.withdraw(5000)
obj.display_balance()"""

#output!:
"""
Balance for dharan:$10000.00
Balance for dharan:$20000.00
Balance for dharan:$15000.00
#output2:
Today you deposited 10000 and your previous balance is 10000 and now your total balance is20000
your withdrawl is 5000 and updated bank balance is 5000
"""
#Real and imaginary operations
#sum(complex_numbers)
#subtraction(complex_numbers)
#product(complex_numbers)

#TRIAL
"""
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def sum(self,other):
        real_sum=self.real+other.real
        imaginary_sum=self.imaginary+other.imaginary
        return f'sum = {real_sum}+{imaginary_sum}'
    
    def sub(self,other):
        real_sub=self.real-other.real
        imaginary_sub=self.imaginary-other.imaginary
        return f'sub = {real_sub}+{imaginary_sub}'
    
    def prod(Self,other):
        real_prod=self.real-other.real
        imaginary_prod=self.imaginary-other.imaginary
        return f'prod = {real_prod}+{imaginary_prod}'

obj=Complex()
print(obj.sum(2,4i))
print(obj.sub(1,2i))
print(obj.prod(3,2i))
"""
#trial 2

class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return Complex(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self,other):
        return Complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self,other):
        #return complex(self.real*other.real,self.imaginary*other.imaginary)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f'{self.real:.2f}'+("+"if self.imaginary>=0 else '')+f'{self.imaginary:.2f}i'
   
a_real,a_imaginary = map(float, input("Enter real and imaginary of first complex number").split())
b_real,b_imaginary = map(float, input("Enter real and imaginary of second complex number").split())
a = Complex(a_real, a_imaginary)
b = Complex(b_real, b_imaginary)

addition = a + b
print("Addition:", addition)

subtraction = a - b
print("Subtraction:", subtraction)


multiplication = a * b
print("Multiplication:", multiplication)
        

"""
#trial3
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real: .2f}" +("+" if self.imaginary>= 0 else "") + f"{self.imaginary: .2f}i"
a_real,a_imaginary = map(float, input("Enter real and imaginary of first complex number").split())
b_real,b_imaginary = map(float, input("Enter real and imaginary of second complex number").split())
a = ComplexNumber(a_real, a_imaginary)
b = ComplexNumber(b_real, b_imaginary)

addition = a + b
print("Addition:", addition)

subtraction = a - b
print("Subtraction:", subtraction)


multiplication = a * b
print("Multiplication:", multiplication)
"""
#output:
"""
Enter real and imaginary of first complex number3 4
Enter real and imaginary of second complex number2 1
Addition: 5.00+5.00i
Subtraction: 1.00+3.00i
Multiplication: 2.00+11.00i"""

#TCS question
#managing showroom paintings by creating two classes painting and showroom
#painting should contains--->id,name,price,type
#showroom should contains--->paintings:A list of painting objects
#showroom class should have one method--->total_price_of_type(paintings_type):returns total price of all paintings of given type
#we have to Accomplish--->
        
        
    
    
        
        


        































































    
    































