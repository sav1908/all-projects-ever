# ===MATH & LOGIC PROGRAMS ===

# Fibonacci sequence
t = int(input("Enter number of terms minus 2 "))
a = 0
b = 1
print(a)
print(b)
for i in range(t):
    a, b = b, a + b
    print(b)

# Factorial
num = int(input("Enter number "))
prod = 1
for j in range(num, 0, -1):
    prod *= j
print(prod)

# Expansion: 1+ x^1/1! + x^2/2! + ... + x^n/n!
n = int(input("Enter number of terms for the expansion 1+ x^1/1! + x^2/2! + ... + x^n/n!  "))
x = int(input("Enter value of x "))
sum = 1
for i in range(1, n):
    prod = 1
    for j in range(i, 0, -1):
        prod *= j
    sum += x**i / prod
print(round(sum))

# Geometric progression sum (a + ar + ar^2 + ...)
n = int(input("Enter no. of terms "))
a = int(input("Enter value of a "))
r = int(input("Enter value of r "))
sum = 0
for i in range(n):
    sum += a * (r ** i)
print(sum)

# Armstrong number check
n = int(input("Enter your number "))
f = n
arm = 0
while f > 0:
    arm += (f % 10) ** 3
    f //= 10
if n == arm:
    print(n, 'is an armstrong number ')
else:
    print("not armstrong ")

# Alternating power series: 1 - x + x^2 - x^3 + ...
sum = 0
x = int(input("Enter value of x "))
n = int(input("Enter value of n "))
for i in range(n + 1):
    if i % 2 == 0:
        sum += x ** i
    else:
        sum -= x ** i
print(sum)
