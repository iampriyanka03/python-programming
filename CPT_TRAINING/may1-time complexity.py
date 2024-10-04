#time complexity
'''for _ in range(5):
    print("pandu")'''
#time complexity :O(5)
# 1. start 0
# 2. comparison
# 3. print
# 4. condition
# 5. comparison


# best,avg,worst case
'''
marks = float(input("enter marks"))
if marks >=90:
    grade = "A"
elif marks >=80:
    grade = "B"
if marks >=70:
    grade = "C"
if marks >=60:
    grade = "D"
if marks >=50:
    grade = "E"
else :
    grade = "F"
'''

#best case : 95 ,worst case : 40 (which takes more iteration time) avg case : lies in b\w best and worst







#asymptotic notations
# 1.O() upper bound(worst case)
# 2.omega lower bound (best case)
# 3.theta average case



#increasing order of runtime
'''1 < logn < n < nlogn < n^2 < n^3 < 2^n < n^n
1 - best case
n^n - worst case'''


#binary search



'''def example(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

to calculate for nested loops n*n
different blocks : n+n'''


'''def func1():
    sum_val = 0
    product = 1
    length = len(array)
    for i in range(length):
        sum_val +=array[i]
    for i in range(length):
        product+=array[i]'''

# here there are seperate loops so time complexity n+n = 2n neglet constants O(n)


'''import random
def function(n):
    if n<=0:
        return 0
    else:
        i = random.randint(0,n-1)
        print("this")
        return function(i) + function(n-i-1)'''

#prime number
'''def is_prime(n):
    if n==1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True'''
#time complexity : O(sqrt(n))




'''def fun(n):
    for i in range(1,n+1):
        j=n
        while j>0:
            j//=2'''



            
