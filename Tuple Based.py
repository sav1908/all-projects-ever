# === TUPLE-BASED PROGRAMS ===

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

