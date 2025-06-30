# ===  FUNCTION-BASED PROGRAMS ===

# Prime check function
def func(pr):
    if pr < 2:
        return False
    elif pr == 2:
        return True
    else:
        for i in range(2, pr // 2):
            if pr % i == 0:
                return False
        else:
            return True
print(func(9))

# Area calculator
def calculate_area(s, b, h):
    if s == 'rectangle':
        area = b * h
    else:
        area = 0.5 * b * h
    return area
s = input("Enter shape type rectangle/triangle ")
b = int(input("Enter base  "))
h = int(input("Enter height "))
print(calculate_area(s, b, h))

# Currency converter
def func(d, dr):
    inr = d * dr
    print(inr)
d = int(input("Enter amt in dollars "))
dr = int(input("Enter rate (1 dollar is how many rupees?) "))
func(d, dr)

# Reverse a string
def reverse(st):
    stn = ""
    a = -1
    for i in st:
        stn += st[a]
        a -= 1
    return stn
st = input("Enter string ")
print(reverse(st))

# Area calculator with menu
men = int(input("MENU OF AREAS \n 1. Rectangle  \n 2. Square  \n 3. Triangle \n 4. Circle \nEnter your choice"))
def rect(l, w):
    area = l * w
    return area
def square(l):
    area = l ** 2
    return area
def tri(b, h):
    area = 0.5 * b * h
    return area
def circ(r):
    area = 3.14 * r ** 2
    return area
if men == 1:
    l = int(input("Enter length "))
    b = int(input("Enter breadth "))
    print(rect(l, b))
elif men == 2:
    l = int(input("Enter length "))
    print(square(l))
elif men == 3:
    b = int(input("Enter breadth "))
    h = int(input("Enter height "))
    print(tri(b, h))
elif men == 4:
    r = int(input("Enter radius "))
    print(circ(r))