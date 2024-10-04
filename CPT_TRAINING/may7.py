# issubsequence 392 (leetcode)
'''def issubsequence(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1
        if i == len(s):
            return True
    else:
        return False
s = input()
t = input()
print(issubsequence(s,t))'''
