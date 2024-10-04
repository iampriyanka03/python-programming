'''def sum_of_odd(lst):
    even=[]
    odd=[]
    sum=0
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            sum+=i
    print(sum)
sum_of_odd([1,2,3,4,5,6,7,8,9,0])'''

'''def count_multiples(m,n):
    multiples=[]
    for i in range(1,n+1):
        if i%m==0:
            multiples.append(i)
    print(multiples)
    cnt=len(multiples)
    print(cnt)
count_multiples(3,30)'''

'''def replace_evens(lst):
    replaced_list = []
    for i in lst:
        if i%2==0:
            replaced_list.append(0)
        else:
            replaced_list.append(i)
    print(replaced_list)
replace_evens([1,2,3,4,5,6,7,8,9])'''

'''def max_element(lst):
    a=max(lst)
    print(a)
max_element([1,2,3,4,5,6,7,8,9])'''

"""def count_elements():
    lst=[1,1,2,2,2,2,2,2,2,3,4,4,4,5,5,5,5,6,7,8,8,8,9,9,9,9]
    target=int(input("enter something"))
    print(lst.count(target))
count_elements()"""


"""inputs = [int(x) for x in sorted(input("enter"))]"""



#string methods
'''str.upper()
str.lower()
str.strip()
str.split()
str.join(iterable)
str.find(substring)
str.replace(old,new)#replace old str with new str
str.endswith(suffix)# true 1 false -1'''

'''str="            donapriyanka          "
a=str.lower()
print(a)
b=str.upper()
print(b)
c=str.split()
print(c)
a=["pandu","teju","dharani","jyo"]
print("_".join(a))
print("*".join(str))'''

'''c="python training"
print([*c])'''


'''a=("pandu")
print(a.join('dona'))
d=a.find("teju") 
print(d)
a=["pandu","teju","dharani","jyo"]
print("_".join(a))'''


#anagram checker
#write a function which takes two strings  as input return true if they are anagram and false otherwise
"""def anagram_checker():
    str1="aabbcc"
    str2="aabbcc"
    for i in str1:
        for j in str2:
            if str(i)==str(j):
                print(True)
            else:
                print(False)
anagram_checker()"""

'''def anagram_checker(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace("", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths are different
    if len(str1) != len(str2):
        return False

    # Sort the characters in each string and compare
    return sorted(str1) == sorted(str2)

# Example usage
str1 = "listen"
str2 = "silent"
print(anagram_checker(str1, str2))  # Output: True'''

'''def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if i not in s2:
            return False
    return True
s1=input("")
s2=input("")
result="Yes" if anagram_check(s1,s2) else "No"
print(result)'''

#pangram
'''import string
def pangram():
    str=input("enter the string")
    for i in str:
        if i in string.ascii_letters:
            return True
        else:
            return False
print(pangram())'''


'''import string
alph=list(string.ascii_lowercase)
str1='helloworld'
str1.lower()
print(all(i in str1 for i in alph))'''



#longest repeating sub string
#write afunction input->string output->longest repeating sub string appears atleast twice
#in input
'''input = abababa
output = aba'''


"""write function tuple operation """
#cal sum of first integer in each tuple
#cal and sum of second integer
#return a tuple with max integer in each tuple

'''def tuple_elements():
    a=[(1,2),(3,4),(5,6)]
    max_tuple=[]
    sum1=0
    sum2=0
    for i in a:
        sum1=sum1+i[0]
        sum2=sum2+i[1]
        max_tuple.append(max(i))
    print(sum1)
    print(sum2)
    print(max_tuple)
    
tuple_elements()'''

#swapping two tuple elements each having exactly two tuples
"""a=((1,2),(3,4))
mutable=list(a)
mutable[0]=(mutable[0][1],mutable[0][0])
mutable[1]=(mutable[1][1],mutable[1][0])
print(tuple(mutable))"""

''''a,b = (int(x) for x in input().split())
print(a,b)'''

'''a=list(map(int,input().split()))
print(a)'''

#to add first and last digit in a number
'''a=int(input())
a_1=str(a)[0]
a_2=str(a)[-1]
print(int(a_1)+int(a_2))'''

#to check wheather specific element is present in list or not
'''l=[1,2,3,4,5]
if 3 in l:
    print("true")
else:
    print("false")'''

#finding with specific index
'''l=[1,2,3,4,5]
if l[2]==3:
    print("true")
else:
    print("false")'''


'''matrix = [[1, 2], [3, 4], [5, 6]]
if [3,4] in matrix:
    print("present")
else:
    print("not present")'''


#bitwise operator:only int and boolean


#skiping vowels
'''a=input()
for i in a:
    if i in "aeiou":
        continue
    print(i)'''


#lists
name = "pandu"
for i in name:
    print(i*i)
    














