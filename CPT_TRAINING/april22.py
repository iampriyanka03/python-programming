#no idea(hackerrank)
'''a=eval(input())
b=eval(input())
m=eval(input())
happiness = 0
for i in a:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1
print(happiness)'''

#find mbc(hackerrank)
'''from math import degrees,atan2
AB=float(input())
BC=float(input())
MBC=
round(degrees(atan2(AB,BC)))
print(MBC,chr(176),sep='')'''    


#palindrome triangle
'''for i in range(1,int(input())+1):
    print(((10**i-1)//9)**2)'''


#numerical triangle
'''for i in range(1,int(input())+1):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

#optimal solution
'''for i in range(1,int(input())):
    print((i*(10**i-1)//9))
#tracing
i = 1 :1*(10**1-1)/9 = 1
i = 2 :11*2 = 22
i = 3 :111*3 = 333
i = 4 :1111*4 = 4444'''

#to find the runner up
'''if __name__ == '__main__':
    n = int(input())
    a = list(set(map(int, input().split())))
    b=sorted(a)
    print(b[-2])'''


#find the count of tallest candle
'''candle=eval(input())
#maxi=max(candle)
print(candle.count(max(candle)))'''
