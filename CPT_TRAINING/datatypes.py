#lists


#append:adds element at the end
'''lst=[]
for i in range(3):
  n=int(input())
  lst.append(n)
  print(lst)'''

#append elements only starts with 5
'''a = []
for i in range(5):
    n = int(input())
    if str(n)[0]=='5':
        a.append(n)
    print(a)'''


#clear : clears all the elements from the list
'''lst = [1,2,3,54,4]
print(lst.clear())'''

#copy : copies from list 
# 1.using copy() method
'''a=[1,2,3,4]
b=[5,6,7,8]
b=a.copy()
print(b)
#  2. using '='
b=a
print(b)'''

#difference between '=' and copy() method
'''list1 = [1,2,3,4]
list2 = list1.copy()
print(list1,list2)
list1.append(200)
print(list1,list2)
list1.clear()
print(list1,list2)

list1=[1,2,3,4]
list2=list1
print(list1,list2)
list1.append(2334)
print(list1,list2)
list1.clear()
print(list1,list2)'''

#count : counts the no of occurances of an element
'''a=[1,1,2,2,3,3,4,4,5,5,5,6,6,7,7,8,8,9,9]
print(a.count(3))'''

# extend : add another list
'''lst = [1,2,3,4,5,6,7]
abc = [8,9]
lst.extend(abc)
print(lst)

lst.extend([11,22,33,44])
print(lst)'''

# index(element) : returns the index of the element
'''lst = [1,2,3,4,5,6,7]
print(lst.index(4))'''

#insert(position,element)
'''list1 = [1,2,3,4,5,6,7]  
list1.insert(4,8)
print(list1)'''


#pop(index)
'''lst = [1,2,3,4,5,6,7]
lst.pop(5)
print(lst)'''

#remove(element)
'''lst = [1,2,3,4,5,6,7]
lst.remove(7)
print(lst)'''


#sorting
'''num = [700,900,500,600,100,800]
num.sort()
print(num)
num.sort(reverse=True)
print(num)'''

#build in functions in list
''''lst=[1,2,3,4,5,6,8,9]
print(sum(lst))
print(min(lst))
print(max(lst))
print(len(lst))'''


#list compression
#syntax : [expression for variable in sequence if condition]
'''name = 'pandu'
list1 = [i for i in name]
print(list1)
print(*list1)'''

'''num=input().split()
even = [i for i in num if int(i)%2==0]
print(even)'''

'''name = input().split()
a = list(name)
a[0]= '9'
a[-1] = '9'
print(''.join(a))

print("9",name[1:-1],"9",sep="")'''

#tuples
'''a=(1,2,3,4,5)
print(type(a))
b=1,23,4,5
print(type(b))
c=(4)
print(type(c))
d=(4,)
print(type(d))'''

#tuple methods
'''a=(1,2,3,4,5)
print(a.count(3))
print(a.index(4))
print(a[3])'''

#dictionaries
'''a ={1:"pandu",2:"piggy"}
print(a)
print(type(a))
b = dict({1:100,2:200})
print(type(b))
print(b[1])'''

# adding new element to the dictionary
'''employee = {"name" : "pandu" , "empid" : "21KN1A4431"}
print(employee)
employee['salary'] = 10000000
print(employee)
#updating the dictionary
employee['name'] = 'donapriyanka'
print(employee)'''


#dictionary methods : keys() , values() , items() , fromkeys()
'''sample = {1:'c',2:'cpp',3:'java',4:'python'}
print(list(sample.keys()))
print(list(sample.values()))
print(list(sample.items()))
print(sample.fromkeys(range(1,10),"10"))

# dictionaryname.get(key)
print(sample.get(1))'''






















