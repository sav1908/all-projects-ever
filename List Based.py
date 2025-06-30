# === LIST-BASED PROGRAMS ===

# Count frequency using method
l = [3,21,5,6,3,8,21,6]
a = int(input("Enter a no.: "))
if a in l:
    print(l.count(a))
else:
    print("Number not found")

# Count frequency without method
l = [3,21,5,6,3,8,21,6]
a = int(input("Enter a no.: "))
ct = 0
for i in range(len(l)):
    if l[i] == a:
        ct +=1
print(a, "occurs", ct, "times")
if ct == 0:
    print("Number not found")

# Max and min in list
l =[]
n = int(input("How many elements in the list? "))
for i in range(n):
    el = int(input("Enter element "))
    l.append(el)
print("list is: ", l)
max = 0
for i in range(n):
    if l[i] > max:
        max = l[i]
print("Maximum number is: ", max)
min = max
for i in range(n):
    if l[i] < min:
        min = l[i]
print("Minimum number is: ", min)

# Add 5 to odd, 10 to even
l = [10,20,3,100,65,87,1]
for i in range(len(l)):
    if l[i] %2 == 0:
        l[i] += 10
    else:
        l[i] += 5
print(l)

# Unique and duplicate items
l = [2,7,1,4,9,5,1,4,3]
ld = []
i = 0
while i < len(l):
    j = i+1
    while j < len(l):
        if l[i] == l[j]:
            dup = l.pop(j)
            ld.append(dup)
            j -=1
        j +=1
    i += 1
print(l)
print(ld)

# Words starting with 's'
a = input("Enter a sentence: ")
l = a.split()
for i in l:
    if i[0] == 's':
        print(i, end=' ')

# Words starting with vowels
s = input("Enter a string ")
l = s.split()
new = []
for i in l:
    if i[0] in 'AEIOUaeiou':
        new.append(i)
if len(new)>0:
    print("List of vowels:",new)
else:
    print("no vowels")

# Interleaving two lists
l1 = [10,11,12]
l2 = [13,14,15]
l = []
length = len(l1)
for i in range(length):
    l.insert(i,l1[i])
    l.append(l2[i])
print(l)

# Max from two lists
l1 = []
l2 = []
num1 = int(input("How many elements in list 1? "))
for i in range(num1):
    el1 = int(input("Enter element"))
    l1.append(el1)
num2 = int(input("How many elements in list 2? "))
for i in range(num2):
    el2 = int(input("Enter element"))
    l2.append(el2)
a = max(l1)
b = max(l2)
print('list 1 is ',l1, ' and list 2 is ', l2)
if a > b:
    print(a,'is greatest and its index is',l1.index(a),'in list 1')
else:
    print(b,'is greatest and its index is',l2.index(b),'in list 2')

# Max index check
l = [1,7,3,17,6,5,2]
a = l.index(max(l))
half = len(l)//2
if a == half:
    print('value lies in the middle')
else:
    if a > half:
        print("second")
    else:
        print('first')

# Swapping in list
l = [0,1,2,3,4,5,6]
length = len(l)
if length % 2 != 0:
    length -= 1
i = 0
while i < length:
    l[i],l[i+1] = l[i+1],l[i]
    i += 2
print(l)

# List subarray with sum k
list1 = [1, 3, 2, 4, 2, 1]
long = []
k = 8
for i in range(len(list1)):
    temp = []
    for j in range(i+1,len(list1)):
        sub = list1[:i+1]
        sub.append(list1[j])
        if sum(sub) == k and len(sub) > len(long):
            long = sub
print(long)

# List transform by swapping on multiples of 7
l = [1,3,14,5,3,7,18,21,9]
for i in range(len(l)):
    if l[i]%7 == 0:
        l[i],l[i-1] = l[i-1],l[i]
print(l)

# Finding lowest and second lowest
l = []
for i in range(10):
    el = int(input("Enter element "))
    l.append(el)
print(l)
low = 0
for i in l:
    if i > low:
        low = i
for i in l:
    if i < low:
        low = i
print('lowest no. is ',low)
l.remove(low)
seclow = 0
for i in l:
    if i > seclow:
        seclow = i
for i in l:
    if i < seclow:
        seclow = i
print('second lowest no. is ', seclow)