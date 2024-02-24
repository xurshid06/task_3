'''
1
mytuple = ("tuple", 12, True , False, 123)
print(mytuple)
mylist = list(mytuple)
a = input("sonni kiriting, tuplega qo'shib chiqaraman: ")
mylist.append(a)
mytuple = tuple(mylist)
print(mytuple)

2
mytuple = (15, 26, 95, 84,8, 15, 62)
print("tupleda quyidagilar bor: ", mytuple)
a = int(input("sonni kiriting, tupledan o'chiraman: "))
mylist = list(mytuple)
for i in mylist:
    if i == a:
        mylist.remove(i)
mytuple = tuple(mylist)
print(mytuple)


3
a = (15, 26, 95, 84,8, 15, 62)
b = list(a)
b.reverse()
print(b)

4
a = [(10, 20, 40), (40, 50, 60), (70, 80, 90,)]
z = list(a[0])
b = list(a[1])
c = list(a[2])
z.pop()
z.append(100)
b.pop()
b.append(100)
c.pop()
c.append(100)
z = tuple(z)
b = tuple(b)
c = tuple(c)
a[0] = z
a[1] = b
a[2] = c
print(a)

5
a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
a.remove(())
a.remove(())
print(a)

6
a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
a.reverse
print(a)


#======================================list================================

1
list1 = ["behi", "anor", "olma", "ilon", "aka", "behi"] 
for i in list1:
    for a in i:        
        print(i)

2
list1 = ["behi", "anor", "olma", "ilon", "aka", "behi"]
for i in list1:
    for j in i:
        if j == 'a':
            list1.remove(i)
print(list1)

3
son = [15, 48, 87, 21, 212, 1, 74]
yigindi = 0
for i in son:
    yigindi += i
print(yigindi)

4
son = [1, 2, 3, 4]
kopaytma = 1
for i in son:
    kopaytma *= i
print(kopaytma)

5
son1 = [212, 2, 3, 4]    
son2 = [15, 48, 87, 21, 212, 1, 74]
for i in son1:
    for j in son2:
        if i == j:
           son1.remove(i)
           son2.remove(j)
           print(son1)
           print(son2)

6
son1 = [212, 2, 3, 4]    
son2 = [15, 48, 87, 21, 212, 1, 74]
for i in son1:
    for j in son2:
        if i == j:
            print(True)

7
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
for i in son:
    if i % 2 == 1:
        print(i)

8
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
a = random

9
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
print(max(son))

10
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
print(min(son))

11
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
son.sort()
print(son[-2])

12
son = [15, 48, 87, 21, 212, 1, 74, 22, 2, 3, 4]
son.sort()
print(son[1])


13
son = [1, 2, 3, 4, 5, 6, 7]
for i in son:
    z = (i**2)
    print(z)

14
list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list[2][1][2].append(["h", "i", "j"])
print(list)



15
text = "OpenAI GPT-3.5 modeli yuqori sifatli texnologiyadir. Ular yaratilgan so'zlarni, matnlarni va savollarni tushunishga qodir bo'ladi. Bu texnologiya orqali matnlar avtomatik ravishda yaratiladi. Uzunliklari 2 dan 10 tagacha bo'lgan so'zlar ham matnga qo'shilgan. Bu matnda 'OpenAI', 'GPT-3.5', 'modeli', 'sifatli', 'texnologiyadir', 'Ular', 'yaratilgan', 'so\'zlarni', 'matnlarni', 'va' kabi so'zlar mavjud. OpenAI texnologiyalar kompaniyasi tomonidan tuzilgan."

listt = text.split()
soni = int(input("nechta harfli so'zni chiqarish kerak: "))
for i in listt:
    l = len(i)
    if l == soni:
        print(i)

16
matn = "salom python assalom python salom dunyo"
zlist = matn.split()
harf = input("harfni kiriting: ")
soni = 0
for i in zlist:
    for j in i:
        if j == harf:
            soni += 1
            print(i, "da", soni, 'ta')
    soni = 0
    
18
mylist = ['a','b','c']
liss = []
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        liss = mylist[i] + mylist[j]

    print(liss)
'''
19
matn = "salom python assalom python salom dunyo"
uzunsoz = ""
for i in matn.split():
    if len(i) > len(uzunsoz):
        uzunsoz = i
    
   
print(uzunsoz)
'''
son = [1, 344, 54, 95, 6262, 21, 74, 15, 65, 2, 4, 7]
result = []
s = 0
for i in range(len(son)):
    mins = son[]
'''

























































