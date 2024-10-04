#pattern
'''n=int(input())
for i in range(2*n-1):
    for j in range(2*n-1):
#calculating max distance
        distance = max(n-min(i,2*n-2-i),n-min(j,2*n-2-j))
        print(distance,end="")
    print()'''

#optimal solution
'''n=int(input())
for i in range(2*n+1):
    for j in range(2*n+1):
        print(max(n-i,n-j,i-n,j-n)+1,end="")
    print()'''


#lambda function
#syntax : lambda arguments:expression
'''add = lambda x,y : x+y
print(add(1,2))'''

#map function
#map(function, iterable)
'''lst=[2,3,4,5,6]
squares=list(map(lambda n:n**2,lst))
print(squares)'''

#example 2
'''name=['abc','xyz']
name2=list(map(lambda w:w[0].upper()+w[1:],name))
print(name,name2,sep="\n")'''

#example 3
'''element = ["erfewsfer","reerre","ertg"]
elem2 = list(map(lambda n:n[::-1],element))
print(elem2)'''

#sorting
'''result=sorted(input(),key=lambda x:(x.isdigit() and int(x)%2==0,x.isdigit(),x.isupper(),x))
print(''.join(result))'''

#captain room(hackerrank)
'''input()
members = list(map(int,input().split(' ')))
s=set(members)
for i in s:
    members.remove(i)
    if i not in members:
        print(i)
        break'''

#cubing fibonacci series
'''cube = lambda x: x ** 3
def fibonacci(n):
    a,b=0,1
    x=[]
    for i in range(n):
        x.append(a)
        c=a+b
        a,b=b,c
    return x
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))'''

#finding subset
'''set_1={1,2,3,4,5,6,7,8,9}
set_2={3,4,5}
check_subset=set_2.issubset(set_1)
print(check_subset)'''

#modules
#calendar
'''import calendar
month,day,year = map(int,input().split())
dayname = calendar.day_name[calendar.weekday(year,month,day)].upper()
print(dayname)'''


