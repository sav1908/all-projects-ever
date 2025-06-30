# === MISC / STACK SIMULATION ===

# Stack filtering words with no vowels
NoVowel = []
def PushNV(N):
    for i in N:
        for j in i:
            if j in 'AEIOUaeiou':
                break
        else:
            NoVowel.append(i)
N = ['vsf', 'ba', 'lo', 'dsfsdg']
PushNV(N)
while len(NoVowel) > 0:
    a = NoVowel.pop()
    print(a)
print("EmptyStack")

# Stack operations menu
done = False
stem = []
while not done:
    menu = int(input("1.ADD \n 2.DELETE  \n 3.DISPLAY "))
    if menu == 1:
        add = int(input("Enter empno. "))
        stem.append(add)
    elif menu == 2:
        if stem == []:
            print("Cannot delete from empty list ")
        else:
            stem.pop()
    elif menu == 3:
        print(stem)
    else:
        print("please try again dipshit ")
    ask = input("Do you want to continue? ")
    if ask == 'no':
        done = True
    else:
        continue