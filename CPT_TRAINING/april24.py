#employee rating
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/employee-rating-8cd8dc10/
'''def solve(n,workload):
    max_consecutive = 0
    consecutive = 0
    for i in range(n):
        if workload[i]>6:
            consecutive+=1
            max_consecutive = max(max_consecutive,consecutive)
        else:
            consecutive = 0
    return max_consecutive
n=int(input())
workload=list(map(int,input().split()))
print(solve(n,workload))'''


#valid or invalid truck number
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/



#zoos question
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/


#hallow square pattern
'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/the-confused-monk/
'''import math
a=int(input())
b=int(input())
c=a*b
d=math.gcd(a,b)
print(c**d)'''

'''from math import prod,gcd
n=int(input())
elements=list(map(int,input().split()))
a=prod(elements)
b=gcd(*elements)
print(pow(a,b))'''


#riya's birthdsy party
#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/riyas-birthday-party-1/
'''t = int(input("enter the test cases"))
for i in range(t):
    n=int(input("enter the value of n test case {}".format(i+1)))
    print((n*(2*n-1))%(10**9+7))'''


#bitwise operater
#binary decimal conversions
#binary addition,subtraction

'''a=60
b=30
print(a&b)
print(a|b)
print(a^b)
print(a<<1)
print(b>>1)'''


#lonely integer(algorithms hackerrank)
'''def lonelyinteger(a):
    result = 0
    for num in a:
        result^=num
    return result
a=[1,2,3,4,3,2,1]
print(lonelyinteger(a))'''





 














 
