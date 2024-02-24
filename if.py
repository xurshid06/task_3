'''
1
a = int(input("butunson kiriting: "))
if 0 < a:
    print(a + 1)

2
a = int(input("butunson kiriting: "))
if 0 < a:
    print(a + 1)
elif 0 == a:
    print(10)
else:
    print(a - 2)
3
a = int(input("butunson kiriting: "))
if 0 < a:
    print(a + 1)
elif 0 == a:
    print(10)
else:
    print(a - 2)

4
a = 5
b = 9
c = -9
mus = 0
if 0 < a:
    mus += 1
if 0 < b:
    mus += 1
if 0 < c:
    mus += 1
print(res)

5
a = 5
b = 9
c = -9
mus = 0
manfi = 0
if 0 < a:
    mus += 1
elif 0 > a:
    manfi += 1    
if 0 < b:
    mus += 1
elif 0 > b:
    manfi += 1
if 0 < c:
    mus += 1
elif 0 > c:
    manfi += 1
print(res)

6
a = 5
b = 9
if a > b:
    print(a, "katta son")
else:
    print(b, "katta son")

7
a = 5
b = 9
if a > b:
    print(b, "kichik son ")
else:
    print(a, "kichik son")

8
a = 5
b = 9
if a > b:
    print(a, "katta son")
else:
    print(b, "katta son")
if a > b:
    print(b, "kichik son ")
else:
    print(a, "kichik son")
    
9
a = 10
b = 5
c = b
b = a
a = c
print(b, "katta", a, "kichik")

10
a = 10
b = 5
oz1 = 6
oz2 = 8
if oz1 == oz2:
    print(a, b)
else:
    a += oz1+ oz2
    b += oz1+ oz2
print(a, b)

11
a = 10
b = 5
oz1 = 6
oz2 = 8
if oz1 != oz2:
    a += oz2
    b += oz2

print(a, b)
 
12
a = 10
b = 5
c = 18

if a > b:
    if c > b:
        print(b, "eng kichik")
    else:
        print(c, "eng kichik")
elif a > c:
    print(c, "eng kichik")
else:
    print(a, "eng kichik")

13
a = 10
b = 5
c = 18
if a > b and a < c or a > c and a < b:
    print(a, "o'rtacha son")
if a > b and b > c a < b and b < c:
    print(b, "o'rtacha son")
if a > c and c > b or a < c and c < b
    print(c, "o'rtacha son")
    

14
a = 40
b = 59
c = 188
if a > b:
    if a > c:
        print(a, "eng katta")
    else:
        print(c, "eng katta son")
elif b > c:
    print(b, "eng katta son")
else:
    print(c, "eng katta son")
    
if a > b:
    if c > b:
        print(b, "eng kichik")
    else:
        print(c, "eng kichik")
elif a > c:
    print(c, "eng kichik")
else:
    print(a, "eng kichik")

15
a = 40
b = 59
c = 188
if a < b < c or b < a < c:
    print((c+b), (c+a), "eng katta yig'indi")
elif b < c < a or c < b < a:
    print(c+a, a+b, "eng katta yig'indi")
elif a < c < b or c < a < b:
    print(b+c, b+a, "eng katta yig'indi")

16
a = 85
b = 46
c = 138
if a < b < c:
    print(a*2, b*2, c*2, "o'sish tartibida")
else:
    print(a/2, b/2, c/2, "o'sish tartibida emas")

17
a = 85
b = 46
c = 138
if a < b < c or a > b > c:
    print(a*2, b*2, c*2, "o'sish tartibida")
else:
    print(a/2, b/2, c/2, "o'sish tartibida emas")    

18
a = 85
b = 46
c = 85
if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)

19
a = 85
b = 46
c = 85
d = 85
if a == b and a == c:
    print(d)
elif a == c and a == d:
    print(b)
elif b == c and b == d:
    print(a)
elif b == c and b == a:
    print(d)    

20
a = 10
b = 26
c = 48
if ((a+c)/2) > b:
    print("eng yaqin nuqta A va B" )
else:
    print("eng yaqin nuqta B va C")
print("orasidagi masofa =", c - a)

########## 21, 22, 23 tushunolmadim
28
a = int(input("yilni kiriting: "))
kabisa = a // 4
kun = a * 365
print(f"{a} yilda {kun + kabisa} kun bor")

29
son = int(input("son kiriting"))
if son > 0:
    if son % 2 == 0:
        print("kiritilgan son musbat juft son")
    else:
        print("kiritilgan son musbat toq son")
elif son < 0:
    if son % 2 == 0:
        print("kiritilgan son manfiy juft son")
    else:
        print("kiritilgan son manfiy toq son")
else:
    print("0 ga teng")
  
30
for i in range(1, 999):
    if 9< i < 100:
        if i % 2 == 0:
            print(i)
for i in range(1, 999):
    if 99 < i < 1000:
        if i % 2 == 1:
            print(i)        
'''   





















































