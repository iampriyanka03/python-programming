'''class Mycomplex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return Mycomplex(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return Mycomplex(self.real-other.real,self.imag-other.imag)
    def __mul__(self,other):
          real_part = self.real * other.real - self.imag * other.imag
          imaginary_part = self.real * other.imag + self.imag * other.real
          return Mycomplex(real_part, imaginary_part)
    def __str__(self):
        return f"{self.real: .2f}" +("+" if self.imag>= 0 else "") + f"{self.imag: .2f}i"
a_real,a_imaginary = map(float, input("Enter real and imaginary of first complex number").split())
b_real,b_imaginary = map(float, input("Enter real and imaginary of second complex number").split())
a = Mycomplex(a_real, a_imaginary)
b = Mycomplex(b_real, b_imaginary)


addition=a+b
print("Addition:", addition)

subtraction = a - b
print("Subtraction:", subtraction)


multiplication = a * b
print("Multiplication:", multiplication)
'''

#TCS question
#managing showroom paintings by creating two classes painting and showRoom
#painting should contains----> id,name,price,type
#showRoom should contains---->paintings:A list of paintings objects
#showRoom class should also have one method----> total_price_of_type(paintings_type):returns total price of all paintings of given type
#we have to accomplish---->take no.of paintings from  user .take details for each painting(id name type price) and create objects.create showrooom object.take painting type
#print total price of painting of given type.if no painting of given type are found print "painting not found"

'''class painting:
    def __init__(self,num,name,price,painting_type):
        self.num=num
        self.name=name
        self.price=price
        self.painting_type=painting_type
class showRoom:
    def __init__(self):
        self.paintings={}
    def add_painting(self,painting_id,painting_name,painting_price,painting_type):
        self.painting[painting_id]={
            'name':painting_name
            'price':painting_price
            'type':painting_type
        }
    def total_price_of_type(self,painting_type):
        total_price=sum(painting['price'] for painting in self.paintings.values() if painting['type']==painting_type)
        return total_price if total_price>0 else None
        
        
    
'''
#sum vs Xor
def sumXor(n):
       return 2**(bin(n).lstrip('0b').count('0'))
n=int(input())
print(sumXor(n))
