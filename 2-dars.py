'''
1
a = int(input('son kiriting: '))
if a>0:
    print(True)
else:
    print(False)

2    
a = int(input('son kiriting: '))

b = a%2
if b>0:
    print(True)
else:
    print(False)
3
a = int(input('son kiriting: '))
b = a%2
if b==0:
    print(True)
else:
    print(False)
4
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
if a>2 and b<=3:
    print(True)
else:
    print(False)
5
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
if a>=0 and b<-2:
    print(True)
else:
    print(False)
6
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
if a<=b<=c:
    print(True)
else:
    print(False)
7
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
if a>b<c:
    print(True)
else:
    print(False)

8
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))

c = a%2==b%2
if c>0:
    print(True)
else:
    print(False)

9
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = a%2
d = b%2
if c>0 or d>0:
    print(True)
else:
    print(False)

10
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = a%2
d = b%2+c
if d==1:
    print(True)
else:
    print(False)

11
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = a%2
d = b%2+c
if d==0 or d==2:
    print(True)
else:
    print(False)

12
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
d = (a%2)+(b%2)+(c%2)
if d==0:
    print(True)
else:
    print(False)

13
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
d = (a%2)+(b%2)+(c%2)
if d<3:
    print(True)
else:
    print(False)

14
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
d = (a%2)+(b%2)+(c%2)
if d==2:
    print(True)
else:
    print(False)

15
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
d = (a%2)+(b%2)+(c%2)
if d==1:
    print(True)
else:
    print(False)

16
a = int(input('son kiriting: '))

b = a%2
if b==0 and 9<a<100:
    print(True)
else:
    print(False)

17
a = int(input('son kiriting: '))

b = a%2
if b==1 and 99<a<1000:
    print(True)
else:
    print(False)

18
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))

if a==b or a==c or b==c:
    print(True)
else:
    print(False)

19
a = int(input('a sonni kiriting: '))
b = int(input('b sonni kiriting: '))
c = int(input('c sonni kiriting: '))
a1 = 0-a
b1 = 0-b
c1 = 0-c
if b==a1 or b==c1 or a==b1 or a==c1 or c==a1 or c==b1:
   print(True)
else:
    print(False)

20
a = int(input('uch xonali sonni kiriting: '))
a3 = a%10
a1 = a//100
a2 = (a//10)%10
if a1!=a2 and a1!=a3 and a2!=a3:
   print(True)
else:
    print(False) 

21
a = int(input('uch xonali sonni kiriting: '))
a3 = a%10
a1 = a//100
a2 = (a//10)%10

if a1+1==a2 and a2+1==a3:
   print(True)
else:
    print(False) 

22
a = int(input('uch xonali sonni kiriting: '))
a3 = a%10
a1 = a//100
a2 = (a//10)%10

if a1+1==a2 and a2+1==a3 or a1-1==a2 and a2-1==a3:
   print(True)
else:
    print(False)

23
a = int(input('uch xonali sonni kiriting: '))
a3 = a%10
a1 = a//100
a2 = (a//10)%10

if a1==a3:
   print(True)
else:
    print(False)

#24
#a = int(input('a sonni kiriting(0dan katta bo\'lsin): '))
#b = int(input('b sonni kiriting: '))
#c = int(input('c sonni kiriting: '))

25
a = int(input('x sonni kiriting: '))
b = int(input('y sonni kiriting: '))
if x<0 and y>0:
    print(True)
else:
    print(False)

26
x = int(input('x sonni kiriting: '))
y = int(input('y sonni kiriting: '))
if x>0 and y<0:
    print(True)
else:
    print(False)

27
x = int(input('x sonni kiriting: '))
y = int(input('y sonni kiriting: '))
if x<0:
    print(True)
else:
    print(False)

28
x = int(input('x sonni kiriting: '))
y = int(input('y sonni kiriting: '))
if x<0 and y<0 or x>0 and y>0:
    print(True)
else:
    print(False)

29

30
a = int(input('uchburchakning a tomonini kiriting: '))
b = int(input('uchburchakning b tomonini kiriting: '))
c = int(input('uchburchakning c tomonini kiriting: '))

if a==b==c:
    print(True)
else:
    print(False)

31
a = int(input('uchburchakning a tomonini kiriting: '))
b = int(input('uchburchakning b tomonini kiriting: '))
c = int(input('uchburchakning c tomonini kiriting: '))

if a==b or a==c or b==c:
    print(True)
else:
    print(False)

32
a = int(input('uchburchakning a tomonini kiriting: '))
b = int(input('uchburchakning b tomonini kiriting: '))
c = int(input('uchburchakning c tomonini kiriting: '))


if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print(True)
else:
    print(False)

33
a = int(input('uchburchakning a tomonini kiriting: '))
b = int(input('uchburchakning b tomonini kiriting: '))
c = int(input('uchburchakning c tomonini kiriting: '))

if a==b==c:
    print(True)
else:
    print(False)

34
x = int(input('x kordinata  sonni kiriting: '))
y = int(input('y kokrdinata sonni kiriting: '))
if 0<x<9 and 0<y<9:
    z = (x+y)%2                       # yig'indi toq bolsa qora juft bo'lsa oq rangda 
    if z>0:
        print(True)
    else:
        print(False)

else:
    print("xato son kiritdingiz")

35
x1 = int(input('x1 kordinata  sonni kiriting: '))
y1 = int(input('y1 kokrdinata sonni kiriting: '))
x2 = int(input('x2 kordinata  sonni kiriting: '))
y2 = int(input('y2 kokrdinata sonni kiriting: '))
if 0<x1<9 and 0<y1<9 and 0<x2<9 and 0<y2<9:
    z1 = (x1+y2)%2
    z2 = (x2+y2)%2              # yig'indi toq bolsa qora juft bo'lsa oq rangda 
    if z1>0 and z2>0:
        print(True)
    else:
        print(False)

else:
    print("xato son kiritdingiz")

36
x1 = int(input('x1 kordinata  sonni kiriting: '))
y1 = int(input('y1 kokrdinata sonni kiriting: '))
x2 = int(input('x2 kordinata  sonni kiriting: '))
y2 = int(input('y2 kokrdinata sonni kiriting: '))
if 0<x1<9 and 0<y1<9 and 0<x2<9 and 0<y2<9:
                                                        # yig'indi toq bolsa qora juft bo'lsa oq rangda 
    if x1==x2 or y1==y2:
        print(True)
    else:
        print(False)

else:
    print("xato son kiritdingiz")
'''
37
x1 = int(input('x1 kordinata  sonni kiriting: '))
y1 = int(input('y1 kokrdinata sonni kiriting: '))
x2 = int(input('x2 kordinata  sonni kiriting: '))
y2 = int(input('y2 kokrdinata sonni kiriting: '))
if 0<x1<9 and 0<y1<9 and 0<x2<9 and 0<y2<9:                                                   
    if x1-x2==1,-1 and y1-y2 == 1,-1:
        print(True)
    elif x1==x2 and y1==y2:
        print("kordinatalar bir xil kiritildi")
    else:
        print(False)

else:
    print("xato son kiritdingiz")































































