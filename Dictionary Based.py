# === DICTIONARY-BASED PROGRAMS ===

# Sort dictionary by keys
d = {5: "peter", 10: "tony", 1: "steve", 30: "natasha"}
l = list(d.keys())
l.sort()
newdict = {}
for i in range(len(l)):
    newdict[l[i]] = d[l[i]]
print(newdict)

# Convert two lists into a dictionary
l1 = [1, 2, 3, 4, 5]
l2 = ['peter', 'tony', 'bruce', 'natasha', 'steve']
d = {}
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print(d)

# Convert dictionary to a single list
d = {1: 'peter', 2: 'tony', 3: 'bruce', 4: 'natasha', 5: 'steve'}
l1 = []
for i in d:
    l1.append(i)
    l1.append(d[i])
print(l1)

# Frequency dictionary from string
s = 'aba1ccdb'
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] = d[s[i]] + 1
    else:
        d[s[i]] = 1
print(d)

# Dictionary of students and delete entry
num = int(input("How many entries? "))
d = {}
for i in range(num):
    k = input("Enter student name ")
    v = int(input("Enter % "))
    d[k] = v
print(d)
delete = input("Enter a valid student name to delete ")
for i in d.keys():
    if i == delete:
        d.pop(i)
        break
print(d)

# Dictionary max key by frequency (random)
import random
d = {}
for i in range(5):
    a = random.randrange(1,6)
    if a in d:
        d[a] = d[a] + 1
    else:
        d[a] = 1
print(d)
val = 0
key = 0
for i in d:
    if d[i] > val:
        val = d[i]
        key = i
print(key)

# Dictionary number to words
num = input("Enter number ")
numname = ''
name = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
for i in num:
    for j in name:
        if int(i) == j:
            numname += name[j] + ' '
print(numname)

# Sort dictionary values and keys together
d = {'jan': 31, 'feb':28 , 'mar': 31, 'apr': 30, 'may':31, 'june': 30, 'july':31, 'aug':31, 'sep':30, 'oct': 31, 'nov': 30, 'dec':31}
lv = []
lk = []
for i in d:
    if len(lv) == 0:
        lv.append(d[i])
        lk.append(i)
    else:
        for j in range(len(lv)):
            if lv[j] > d[i]:
                lv.insert(j, d[i])
                lk.insert(j, i)
                break
        else:
            lv.append(d[i])
            lk.append(i)
print(lv, lk)

# Month days lookup
mon = input("Enter a month name ")
for k in d:
    if mon == k:
        print('there are ', d[k],'days in ',mon)

# Dictionary of coordinate points
mp = {'a': (4,3), 'b': (1,2), 'c': (5,1)}
lv = mp.values()
maxx = 0
maxy = 0
for i in lv:
    if i[0] > maxx:
        maxx = i[0]
    if i[1] > maxy:
        maxy = i[1]
print('max x value is ', maxx, 'max y value is ', maxy)


# === 4. TUPLE-BASED PROGRAMS ===

# Max, min, sum, mean from tuple
el = int(input("Enter elements "))
t = ()
for i in range(el):
    a = int(input("Enter number "))
    t += (a,)
print ("Max number is", max(t), "min number is", min(t), "sum of numbers is", sum(t), "mean of numbers is", sum(t)/len(t))

# Swap tuples
t1 = ()
num = int(input("How many elements? "))
for i in range(num):
    el = int(input("Enter element "))
    t1 += (el,)
print(t1, 'is tuple 1')
t2 = ()
num = int(input("How many elements? "))
for i in range(num):
    el = int(input("Enter element "))
    t2 += (el,)
print(t2, 'is tuple 2')
t1, t2 = t2, t1
print(t1, 'is tuple 1 now and', t2,'is tuple 2 now')

# Tuple sum of adjacent elements
t = (1,3,4,6,9,10)
length = len(t)
sumt = ()
i = 0
s = 0
while i < length-1:
    s = t[i] + t[i+1]
    sumt += (s,)
    i += 1
print(sumt)

# Tuple Cartesian product
t1 = (1,3)
t2 = (1,4)
l = []
for i in t1:
    for j in t2:
        l.append((i,j))
print(l)

# Tuple of primes and palindromes
t = ()
tprime = ()
tpalin = ()
tn = int(input("Enter no. of el "))
for i in range(tn):
    el = int(input("Enter element "))
    t += (el,)
for j in t:
    if j < 2:
        continue
    for k in range(2,j//2 + 1):
        if j%k == 0:
            break
    else:
        tprime += (j,)
print('tuple of primes is ', tprime)
for a in tprime:
    if str(a) == str(a)[::-1]:
        tpalin += (a,)
print('tuple of prime palindromes is', tpalin)
