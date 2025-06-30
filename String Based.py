# === STRING-BASED PROGRAMS ===

# Longest word in a string
s = input("Enter a string ")
l = s.split()
long = ''
for i in l:
    if len(i) > len(long):
        long = i
print("Longest substring is", long)

# Count number of 'is'
s = input("Enter a string ")
l = s.split()
ct = 0
for i in l:
    if i == 'is':
        ct += 1
print("Number of is's is", ct)

# Palindrome check
s = input("Enter a string ")
for i in range(len(s)//2):
    l = -1
    if s[i] != s[l]:
        print("not a palindrome")
        break
    else:
        l -=1

# Count characters in string
s = input("Enter a string ")
l = 0
for i in s:
    l +=1
print(l)

# Check if string contains digits
s = input("Enter a string ")
for i in s:
    if i in '0123456789':
        print('contains digits')
        break

# Longest word from multiple-word string
s = input("Enter a string with multiple words ")
l = 0
str =''
lis = s.split()
print(lis)
for i in lis:
    if len(i) > l :
        str = i
        l = len(i)
print(str)

# Longest common substring
s1 = input("Enter string 1 ")
s2 = input("Enter string 2 ")
mx = 0
ms = ''
for i in range(len(s1)):
    for j in range(len(s2)):
        temp = ''
        x, y = i, j
        while x < len(s1) and y < len(s2) and s1[x] == s2[y]:
            temp += s1[x]
            x+= 1
            y +=1
        if len(temp) > mx:
            mx = len(temp)
            ms = temp
print(ms, mx)

# Remove vowels from string
s = input("Enter a string ")
l = ''
for i in s:
    if i not in "AEIOUaeiou":
        l += i
print(l)

# Replace vowels with *
str1 = input("Enter a string ")
str2 = ''
for i in str1:
    if i not in 'AEIOUaeiou':
        str2 += i
    else:
        str2 += '*'
print(str2)

# Toggle case
str1 = input("Enter a string ")
str2 = ''
for i in str1:
    if i.isupper():
        str2 += i.lower()
    elif i.islower():
        str2 += i.upper()
    else:
        str2 += i
print(str2)