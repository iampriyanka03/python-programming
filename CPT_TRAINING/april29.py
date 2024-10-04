'''file = open("files.txt","r") #open a file
#content = file.read() # reading entire document
#content = file.readlines() #lines into the list
#content = file.readline() #reading one line
print(content)'''

'''file = open("files.txt","w")
#write to the file
file.write("thanks replit \n")
file.close()'''

'''with open('files.txt','r') as file:
  content = file.read()
  print(content)'''

#python's with statement ensures that the file is properly closed after its suite finisher, even if an exception occurs.

#create a files.txt file

'''from abc import ABC,abstractmethod
class DataProcessor(ABC):
    @abstractmethod
    def read_data(self,filename):
        pass
    def write_data(self,data,filename):
        pass
class CSVprocessor(DataProcessor):
    def read_data(self,filename):
        with open(filename,'r') as file:
            return file.read()
    def write_data(self,data,filename):
        with open(filename,'w') as file:
            return write(data)'''

#exception handling
'''def safe_divide():
    try :
        numerator=int(input())
        denominator=int(input())
        print(numerator/denominator)
    except ValueError :
        print("both numerator and denominator must be integers")
    except ZeroDivisionError :
        print("cannot divide by zero")
safe_divide()'''



'''class ZeroDivisionError(Exception):
    pass
def is_integer(value):
    try :
        int(value)
        return True
    except ValueError :
        return False

def safe_divide(numerator,denominator):
    try:
        if not(is_integer(numerator) and is_integer(denominator)):
            raise ValueError('both num and den must be integer')
        if denominator == 0:
            raise ZeroDivisionError("cannot divide by zero")

        result = int(numerator) / int(denominator)
        return result
    except ValueError as ve:
        return str(ve)
    except ZeroDivisionError as zde:
        return str(zde)

print(safe_divide(10,2))
print(safe_divide(10,0))
print(safe_divide(10,'a'))'''

#compare the triplet (hackerrack)
'''alice = [i for i in input().split()]
bob =   [j for j in input().split()]
alice_count = 0
bob_count = 0
if alice[0] > bob[0]:
    alice_count+=1
elif alice[1] == bob[1]:
    print("nobody recieves a point")
else:
    bob_count+=1
print(alice_count,bob_count)'''
    
    
    
    





















    
