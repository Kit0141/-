#---------------------------------------1-----------------------------------------------------
a = 0
while a < 100 :
    a = a + 1
    if a % 7 == 0:
            print(a)
#-------------------------------------------------------------2-----------------------------------------

b1 = input(str('Имя: '))
b2 = input(str('Пол: '))
c = []#муржкой
d = []#женский
o = 0
while o <= 5:
    print(b1)
    print(b2)
    if b2 == 'man':
        c.append(b1)
        c.append(b2)
    elif b2 == 'woman':
        d.append(b1)
        d.append(b2)

    o = o+1
   # -------------------------------------------------3-----------------------------------------------------------

    a = str(input("Напишите: "))
    b = ""
    for c, z in enumerate(a):
        if c % 2 == 0:
            print(c)

   # ----------------------------------------------4-------------------------------------------


vse = ['kartoshka', 'smorodina', 'yabloki', 'grushi','morkovka', 'luk', 'pomidor', 'apelsini','arbuz']
ovoshi = ['kartoshka', 'morkovka', 'luk', 'pomidor']
frukti = ['yabloki', 'grushi', 'apelsini']
d = ""

for d in vse:
    if ovoshi in vse:
        print(d, "это овощ")
    elif frukti in vse:
        print(d, "это фрукт")
    else:
        print(d, "это ягода")
