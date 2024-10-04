#library management system
'''class library:
    def __init__(self,name,books):
        self.name=name
        self.books = books
    def add_book(self,book_title):
        if book_title not in self.books:
            print(f"book '{book_title}' added to the library")
        else:
            print(f"book '{book_title}' is already in the  library")
    def remove_book(self,book_title):
        if book_title in self.books:
            self.book.remove(book_title)
            print(f"book '{book_title}' removed from the library  library")
        else:
            print(f"book '{book_title}' is not in the  library")
    def book_list(self):
        print("books avail in lib")
        print(".\n" .join(self.books))
    #else:
        #print("no books avail in library")

    def search_book(self,book_title):
        if book_title in self.books:
            print(f"book '{book_title}' is avail the library")
        else:
            print(f"book '{book_title}' is not in the  library")
    def display_info(self):
        print(f"library name : {self.name}")
        print(f"no of books {len(self.books)}")

obj=library("pandu",["book1","book2","book3","book4"])
obj.display_info()
obj.add_book("book5")
obj.display_info()
obj.remove_book('book5')
obj.book_list()
obj.display_info()
obj.search_book('book1')
obj.display_info()'''


'''class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __tdiv__(self,other):
        denominator = other.real ** 2 +other.imaginary**2
        real_part = (self.real * other.real +self.imaginary*other.imaginary)/denominator
        imag_part = (self.imaginary * other.real - self.real*other.imaginary)/denominator
        return ComplexNumber(real_part,imag_part)

    def __str__(self):
        return f"{self.real: .2f}" +("+" if self.imaginary>=0 else "") + f"{self.imaginary: .2f}i"
a_real,a_imaginary=(float(x) for x in input().split())
b_real,b_imaginary=(float(x) for x in input().split())
a = ComplexNumber(a_real,a_imaginary)
b = ComplexNumber(b_real,b_imaginary)

division = a.__tdiv__(b)
print("division",division)'''


#SumXor
'''def sumxor(n):
    count = 0
    while n:
        if n % 2 == 0:
            count += 1
        n //= 2
    return 2 ** count
print(sumxor(5))'''

#abstraction - showing only essential data
'''class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.ckutch = True
        self.acc = True
        print("car started")
car1 = Car()
car1.start()'''



'''from abc import ABC,abstractmethod
class Baseclass(ABC):
    @abstractmethod
    def method_1(self):
        pass'''


'''from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return "woof!"
class cat(animal):
    def sound(self):
        return "meow!"
obj = dog()
print(obj.sound())
obj = cat()
print(obj.sound())'''

#concrete sub class class are which has complete implementation
#abstract class cannot create object



'''
from abc import ABC,abstractmethod
#abstract base class
class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    @abstractmethod
    def printdetails(self):
        pass
#concrete sub class
class back(car):
    #concrete sub class(complete implementation of abstract method)
    def printdetails(self):
        print("brand: ",self.brand)
        print("model: ",self.model)
        print("year: ",self.year)

#concrete sub class
class cab(car):
    #concrete sub class(complete implementation of abstract method)
    def printdetails(self):
        print("brand: ",self.brand)
        print("model: ",self.model)

        print("year: ",self.year)

obj = back("mercedes","g-class",2020)
obj.printdetails()'''



#area of shapes
'''from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        print("area of rectangle",self.length*self.breadth)
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("area of circle",3.14*self.radius**2)
obj = rectangle(5,4)
obj.area()
obj = circle(4)
obj.area()'''

#resume worded (score of resume)



        
        
        
        



    
        
    

    
