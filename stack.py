'''#1

Stu={1:56,2:45,3:78,4:65,5:35,6:90}
stack_Roll=[]
stack_Marks=[]
def Push_Stu(stu):
    for i in stu:
        if stu[i] > 60:
            stack_Roll.append(i)
            stack_Marks.append(stu[i])
def Pop_Stu(stack_Roll,stack_Marks):
    if len(stack_Roll) > 0 and len(stack_Marks) > 0:
        stack_Roll.pop()
        stack_Marks.pop()
        print(stack_Roll,stack_Marks)
    else:
        print('underflow ')

Push_Stu(Stu)
Pop_Stu(stack_Roll,stack_Marks)

#2
l = [['invincible','skybound','1299'],['batman','dc','499'],
['spiderman','marvel','600'],['the boys','vought','300']]

BOOK = []

def Push_Rec(BOOK):
    for i in l:
        if int(i[2]) > 500:
            BOOK.append([i[0],i[1]])

def Pop_Rec(BOOK):
    if len(BOOK) > 0:
        while BOOK:
            print(BOOK.pop())
        print("Stack Underflow ")

    else:
        print("Stack Underflow ")

Push_Rec(BOOK)
print(BOOK)
Pop_Rec(BOOK)


#3
lst = [['Shiven',80,'Maths'],['Arjun',79,'CS'],['Advik',95,'Bio'],['Arnav',70,'CS'],['Ishan',99,'CS'] ]

Status = []

def Push_Rec(Status):
    for i in lst:
        if i[1] > 75:
            Status.append([i[0],i[1]])

def Pop_Rec(Status):
    if len(Status) > 0:
        while Status:
            print(Status.pop())
        print("Stack Empty ")

#4



list1 = [[1,'sav','18/01/2008','XII'],[2,'fortrex','29/04/2008','XII'],
[3,'vienna','11/03/2008']]

status = []

def Push_el(status):
    no = int(input("How many push operations? "))
    for i in range(no):
        a = int(input("Enter the roll no. of the student u want pushed: "))
        status.append(list1[a-1])

def Pop_el(status):
    if len(status) > 0:
        while status:
            print(status.pop())
        print("Stack empty ")

    else:
        print("Stack empty ")

Push_el(status)
print(status)
Pop_el(status)
'''
#5


stc = []
def pushst(N):
    for i in N:
        if i%2 == 0:
            stc.append(i)

def popst(stc):
    if len(stc) > 0:
        while stc:
            print(stc.pop())

N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
pushst(N)
popst(stc)


#6
R={'RILEY':76, 'JAI':45, 'BOB':89, 'LEO':65, 'AMY':90, 'TOM':82}
stack = []

def push(R):
    for i in R:
        if R[i] > 75:
            stack.append(i)

def pop(stack):
    if len(stack) > 0:
        while stack:
            print(stack.pop())
        print("Stack Empty ")

push(R)
pop(stack)

#7
tl = []
def push_na(Lname,Lage):

    for i in range(len(Lage)):
        if Lage[i] > 50:
            t = ()
            t += (Lname[i],Lage[i],)
            tl.append(t)
    print(tl,'is list of people over 50 ')

def pop_na(tl):
    if len(tl) == 0:
        print("Stack underflow ")

    else:
        print(tl.pop()[0],'has been popped')

Lname=['narender', 'jaya', 'raju', 'ramesh', 'amit', 'Piyush']
Lage=[45,23,59,34,51,43]

push_na(Lname,Lage)
pop_na(tl)

#8

def AddCustomer(NAME,n):
    CStack = []
    for i in range(n):
        tl = []
        admno = i
        tl = [NAME[i],admno]
        CStack.append(tl)
    print(CStack)

NAME = ['shruti','vihit','shiven','ishan','arnav','shrriya','jasveen','myra']
AddCustomer(NAME,8)

#9
CStack = [['shruti', 0], ['vihit', 1], ['shiven', 2], ['ishan', 3], ['arnav', 4], ['shrriya', 5], ['jasveen', 6], ['myra', 7]]
def DeleteCustomer(CStack,n):
    for i in range(n):
        print(CStack.pop())
    print(CStack)

DeleteCustomer(CStack,6)

#10
def POP(cities):
    while cities:
        print(cities.pop())

cities =['Delhi', 'Jaipur', 'Mumbai', 'Nagpur']
POP(cities)


#11
def popstack(nol,n):
    lst = []
    for i in range(n):
        lst.append(nol[i])
    while lst:
        print(lst.pop())

nol = [1,2,3,4,5,6,7,8,9]
n = 6
popstack(nol,n)

#12
lst = [1,2,3,4,5,6,7,8,9,10]
def PUSH(A):
    evel = []
    for i in A:
        if i%2 == 0:
            evel.append(i)
    if len(evel) < 1:
        print("Stack underflow ")

    else:
        print(evel)

PUSH(lst)

#13
lst = [1,2,3,4,5,6,7,8,9,10,13,15,17,20,23,25,30]
def Push(A):
    evel = []
    for i in A:
        if i%5 == 0:
            evel.append(i)
    if len(evel) < 1:
        print("Stack underflow ")

    else:
        print(evel)

Push(lst)



#14

lst = [1,2,3,4,5,6,7,8,9,10]
def PUSHODD(A):
    evel = []
    for i in A:
        if i%2 != 0:
            evel.append(i)
    if len(evel) < 1:
        print("Stack underflow ")

    else:
        print(evel)

PUSHODD(lst)


#15
def pushbook(book,book_no,book_title):
        book.append([book_no,book_title])
        print(book)
book = []
book_no = 1
book_title = 'wimpy kid'
pushbook(book,book_no,book_title)

#16
Dbook={"Python":350,"Hindi":200,"English":270,"Physics":600, "Chemistry":550}
def DPUSH(BOOK):
    dl = []
    for i in BOOK:
        if BOOK[i] > 300:
            print(i)
            dl.append(BOOK[i])

    print("Count of stack is: ",len(dl))

DPUSH(Dbook)

#17
Employee ={"Sohan":20000,"Mohan":9000,"Rohan":25000,"Aman":5000}
def EPUSH(EMP):
    dl = []
    for i in EMP:
        if EMP[i] < 15000:
            print(i)
            dl.append(EMP[i])

    print("Count of stack is: ",len(dl))

EPUSH(Employee)


#18
l=[['ravi',26],['raman',36], ['chaman',56]]
def IPUSH(ITEM):
    dl = []
    for i in ITEM:
        if i[1] < 50:
            print(i)
            dl.append(i)

    print("Count of stack is: ",len(dl))

IPUSH(l)


#19
def push35(num):
    tfl = []
    for i in num:
        if i%5 == 0 or i%3 == 0:
            tfl.append(i)
    print(tfl)
    return tfl
def pop35(tfl):
    while tfl:
        print(tfl.pop())
    print("Stack empty ")


num = [10, 6, 14, 18, 30]
tfl = push35(num)
pop35(tfl)

#20
def PushNV(N):
    novowel = []
    for i in N:
        for j in i:
            if j in 'aeiouAEIOU':
                break
        else:
            novowel.append(i)
    return novowel


N = ['DRY','LIKE','RHYTHM','WORK','GYM']
print(PushNV(N))

a = PushNV(N)
while a:
    print(a.pop(), end = ' ')
print("Empty stack ")


#21

def pushname(n):
    stack = []
    for i in range(n):
        el = input("Enter name (no numbers) : ")
        for j in el:
            if j in '1234567890':

                print("Value discarded ")

        else:
            stack.append(el)
    print(stack)

pushname(6)

