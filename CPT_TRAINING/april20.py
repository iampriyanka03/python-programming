#palindrome
'''def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
print(is_palindrome(eval(input(""))))'''

#reverse words
'''def reverse_words():
    str=input("")
    a=str.split()
    b=" ".join(reversed(a))
    print(b)
print(reverse_words())'''


'''def rev(s):
    rev = " ".join(s.split()[::-1])
    return rev
print(rev("the quick brown fox"))'''


#tuple element count
'''def tuple_count(s):
    sum=0
    for i in s:
        sum+=1
    return sum
print(tuple_count(eval(input())))'''


#tuple concatenation
"""def contatination():
    a=(1,2,3)
    b=(4,5,6)
    return tuple(list(a)+list(b))
print(contatination())"""

'''def contatination(a,b):
    return a+b
a=eval(input())
b=eval(input())
print(contatination(a,b))'''

#find tuple element():
'''def find_tuple(s,k):
    for i in s:
        if i==k:
            return True
    else:
        return False

k=int(input("enter element:"))
s=eval(input(""))
print(find_tuple(s,k))'''

'''def concat(s,k):
    return k in s
k=int(input())
s=eval(input())
print(concat(s,k))'''

#swapcase
'''def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)'''

'''def swap_case(s):
    new=[]
    for i in s:
        if i.isupper():
            new.append(i.lower())
        else:
            new.append(i.upper())
    return new
print(swap_case('PaNdU'))'''

#join and split
'''def split_and_join(line):
    return '-'.join(line.split(' '))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)'''
#bin oct dec hex
'''for i in range(1,18):
    print(f'{i}\t{len(bin(i)[2:])}\t{len(oct(i)[2:])}\t{len(hex(i)[2:])}')'''

'''def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i)
        octal=oct(i)[2:]
        hexadecimal=hex(i)[2:].upper()
        binary=bin(i)[2:]
        print(dec.rjust(w),octal.rjust(w),hexadecimal.rjust(w),binary.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)'''


#string mutations
'''def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)'''

#rectangular pattern
'''for i in range(1,6):
    for j in range(5):
        print("*",end="")
    print()'''


#right angle triangle
'''n=int(input())
for i in range(1,n):
    for j in range(i):
        print("*",end="")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1 ):
        print(j,end="")
    print()'''


'''n=int(input())
for i in range(n):
    for j in range(1,i+1):
        print(i,end="")
    print()'''

'''for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''

'''n=int(input())
for i in range(0,n+1):
    print((n-i)*"* ")'''

#inverted numbered right pyramid
'''for i in range(7,0,-1):
    for j in range(1,i):
        print(j,end="")
    print()'''

#star pyramid
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''


#diamond patter
"""n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()"""

#half diamond star pattern
'''n=int(input())
for i in range(1,n+1):
    print("*"*(i),end="")
    print()
for i in range(n,0,-1):
    print("*"*(i),end="")
    print()'''


#binary number triangle
'''n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(str((i+j)%2),end='')
    print()'''
