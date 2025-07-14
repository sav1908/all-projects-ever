#1
def ZeroEndings(SCORES):
    SUM = 0
    for i in SCORES:
        if str(i)[-1] == '0':
            SUM += i
    print(SUM)
SCORES = [200, 456, 300, 100, 234, 678]
ZeroEndings(SCORES)

#2
def oddeve(L):
    l = []
    for i in L:
        if i >= 0:
            l.append(i)
    return l
l =  [4, -1, 5, 9, -6, 2, -9, 8]
print(oddeve(l))

#3
def ARRNG(string):
    newstr = []
    for i in string:
        if i not in newstr:
            newstr.append(i)
    newstr.sort()
    print(''.join(newstr))

ARRNG('corporate')

#4
def rem_keys(D,keylist):
    for i in keylist:
        if i in D:
            D.pop(i)
    print(D)
D = {1:'lol',2:'hi',3:'lmao',4:'rofl'}
keylist = [1,4]
rem_keys(D,keylist)

#5
def count_city(CITY):
    for i in CITY:
        if len(CITY[i]) < 6:
            print(CITY[i].upper())
CITY = {1:"Ahmedabad", 2:"Pune", 3:"Baroda", 4:"Simla", 5:"Surat"}
count_city(CITY)

#6
def countAlpha(String):
    d = {}
    for i in String:
        if i not in d:
            d[i] = String.count(i)
    print(d)

countAlpha('Peter Parker')

#7
def countMY(SUBJECT):
    for i in SUBJECT:
        if len(SUBJECT[i]) >= 5:
            print(SUBJECT[i].upper())
SUBJECT={1:"Hindi",2:"Physics",3:"Chemistry",4:"cs",5:"Math"}
countMY(SUBJECT)

#8
def dispTop(SCORES):
    s = []
    for i in SCORES:
        if SCORES[i] >= 50:
            s.append(i.upper())
    print(s)
SCORES = {'ayan':56, 'raj' :43, 'ankit':18, 'rehan':90, 'kush':0}
dispTop(SCORES)


#9
def distinction(marks):
    for i in marks:
        if marks[i] >= 75:
            print(i.upper())

marks = {'eng':78, 'phy':69, 'chem':74, 'math':75, 'cs':84}
distinction(marks)

#10
def EVEN_LIST(L):
    even_list = []
    for i in L:
        if i%2 == 0:
            even_list.append(i)
    print(even_list)

L = [1,2,3,4,5,6,7,8]
EVEN_LIST(L)

#11
def convert(L):
    for i in range(len(L)):
        if L[i]%2 == 0:
            L[i] = int(L[i]/2)
        else:
            L[i] =int(L[i]*2)
    print(L)
L = [3,4,5,16,9]
convert(L)

#12
def Shift(Lst):
    if len(Lst)%2 == 0:
        for i in range(0,len(Lst),2):
            Lst[i],Lst[i+1] =Lst[i+1],Lst[i]
        print(Lst)
    else:
        for i in range(0,len(Lst)-1,2):
            Lst[i],Lst[i+1] =Lst[i+1],Lst[i]
        print(Lst)
Lst = [2, 4, 1, 6, 5, 7, 9, 2, 3, 10,1]
Shift(Lst)

#13
def INDEX_LIST(L):
    indexList = []
    for i in range(len(L)):
        if L[i] != 0:
            indexList.append(i)
    print(indexList)
L =  [12,4,0,11,0,56]
INDEX_LIST(L)

#14
def index_list(l):
    sum = 0
    for i in l:
        if i%2 != 0:
            sum += i
    print(sum)
l = [1,2,3,4,5,6,7,8,9]
index_list(l)

#15
def itemshift(x):
    a = x.pop(0)
    x.append(a)
    print(x)
x = [1,2,3,4,5,6]
itemshift(x)

#16
def letter_Count(lst):
    d = {}
    for i in lst:
        if i not in d:
            d[i] = lst.count(i)
    print(d)
lst = list("apple")
letter_Count(lst)

#17
def listchange(Arr):
    for i in range(len(Arr)):
        if Arr[i]%2 == 0:
            Arr[i] = 10
        else:
            Arr[i] *= 5
    print(Arr)


Arr=[10,20,23,45]
listchange(Arr)

#18
def listchange(Arr,n):
    for i in range(n):
        if Arr[i]%2 == 0:
            Arr[i] *= 2
        else:
            Arr[i] *= 3
    print(Arr)


Arr= [10,20,30,40,12,11]
n = 6
listchange(Arr,n)


#19
def max_length(string):
    max = ''

    for i in string:
        if len(i) > len(max):
            max = i
    print(max)

l = ['my','name','is','ironman']
max_length(l)

#20
def modlist(l):
    for i in range(len(l)):
        if l[i]%5 == 0:
            l[i] += 10
    return l

l= [3,5,10,12,15]
print(modlist(l))

#21
def R_Shift(Arr,n):
    for i in range(n):
        a = Arr.pop()
        Arr.insert(0,a)
    print(Arr)

Arr= [ 1,2,3,4,5,6]
n = 2
R_Shift(Arr,n)

#22
def RShift(Arr):
    for i in range(len(Arr)):
        if Arr[i]%2 == 0:
            a = Arr.pop(i)
            Arr.insert(0,a)
    print(Arr)

Arr= [ 1,2,3,4,5,6]

RShift(Arr)

#23

def seminar(events):
    sem ={}
    for i in events:
        if events[i] == 'seminar':
            sem[i] = events[i]
    print(sem)

events={'Delhi':'seminar', 'Mumbai':'Party','Dehradun':'Marriage', 'Goa':'seminar'}
seminar(events)

#24

def shift2(l):
    if len(l)> 4:
        a = l[0]
        l[0], l[-2] = l[-2], l[0]
        l[1], l[-1] = l[-1], l[1]
    else:
        print("List is too small ")
    print(l)

l =[4,20,9,78,45,34,76,56]
shift2(l)

#25
def R_Shift(Arr,n):
    for i in range(n):
        a = Arr.pop(0)
        Arr.append(a)
    print(Arr)

Arr=  [2, 15, 3, 14, 7, 9, 19, 6, 1, 10]
n = 4
R_Shift(Arr,n)

#26


def Show_sal(EMP):
    for i in EMP:
        if EMP[i] < 25000:
            print(EMP[i])


EMP = {1: 18000, 2: 25000, 3: 35000, 4: 15000}
Show_sal(EMP)


#27
def SquareList(L):
    sqls = []
    for i in L:
        if i != 0:
            sqls.append(i**2)
    print(sqls)

l = [9,4,0,11,0,6,0]
SquareList(l)


#28
def MaxOne(a,b):
    if int(str(a)[-1]) > int(str(b)[-1]):
        print(a, 'has bigger ones digit')
    else:
        print(b, 'has bigger ones digit')


MaxOne(491,278)


#29
def Word_len(Text):
    t = ()
    for i in Text.split():
        t += (len(i),)
    print(t)

Word_len("Whats good bro")

#30
def countArticles(string):
    tct = 0
    anct = 0
    act = 0
    for i in string.split():
        if i.lower() == 'the':
            tct += 1
        elif i.lower() == 'an':
            anct += 1
        elif i.lower() =='a':
            act += 1
    d = {'the': tct, 'an':anct,'a':act}
    print(d)
countArticles('The logical or is an operator not a literal or a punctuator.')


#31
def vw(string):
    t = ()
    for i in string.split():
        if i[0].lower() in 'aeiou':
            t += (i,)
    print(t)
vw("An apple a day keeps the doctor away")


#32
def oddsum(l):
    sum = 0
    for i in l:
        if i%2 != 0:
            sum += i
    print(sum)

l = [1,2,3,4,5,6,7,8,9]
oddsum(l)

#33
def lowup(string):
    lct = 0
    uct = 0
    for i in string:
        if i.islower():
            lct += 1
        if i.isupper():
            uct += 1
    print(uct,lct)

lowup('Python ProgrammiNg')

#34
def findword(string,search):
    sct = 0
    for i in string.split():
        if i == search:
            sct += 1
    print(search, 'occurs', sct,'times')
findword("Learning history helps to know about history with interest in history",'history')

#35

def findname(name):
    phonebook = {"Alice": "9876543210", "Bob": "9123456780", "Charlie": "9988776655"}
    if name in phonebook:
            del(phonebook[name])
    print(phonebook)

findname('Alice')


#36
def howmany(data,el):
    elct = 0
    for i in data:
        if i == el:
            elct += 1
    print(el,'occurs',elct,'times')

data = [205,240,304,205,402,205,104,102]
el = 205
howmany(data,el)

#37

def MSEARCH(states):
    for i in states:
        if i[0] == 'm':
            print(i)

states = ['mp','wb','mz','mh','up','hr']
MSEARCH(states)

#38
def aoe(values):
    esum = 0
    osum = 0
    for i in values:
        if i%2 ==0:
            esum += i
        else:
            osum += i
    print(esum, osum)
values =  [15, 26, 37, 10, 22, 13]
aoe( values)

#39
def reverse(x):
    revl = []
    for i in range(-1,-1-len(x),-1):
        revl.append(2*x[i])
    print(revl)


x = [4,8,7,5,6,2,10]
reverse(x)
