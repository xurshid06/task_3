'''
1
k = int(input("k son kiriting: "))
n = int(input("n son kiriting: "))
def nk (k, n):
    
    for n in range(k):
        print(k)

nk(k, n)

2
a = int(input("a son kiriting: "))
b = int(input("b son kiriting: "))
if a < b:
    def ab_sonlar(a, b):
        for i in range(a, b+1):
            print(i)
else:
    print("xato son kiritdingiz")
ab_sonlar(a, b)

3
a = int(input("a son kiriting: "))
b = int(input("b son kiriting: "))
if a < b:
    def ab_sonlar(a, b):
        for i in range(b-1, a, -1):
            print(-i)
else:
    print("xato son kiritdingiz")
ab_sonlar(a, b)

4
k = int(input("Bir kilogram konfert narxini kiriting: "))
def konfet(k):  
    for i in range(1, 11):
        narx = i*k
        print(i"kg konfet", narx"som")
konfet(k)

5
k = int(input("Bir kilogram konfert narxini kiriting: "))
def konfet(k):
    for i in range(1, 11):
        narx = (i/10)*k
        print(i/10, "kg konfet", narx, "som")
konfet(k)

7
a = int(input("a son kiriting: "))
b = int(input("b son kiriting: "))
if a < b:
    def ab_sonlar(a, b):
        for i in range(a, b):
            print(i)
else:
    print("xato son kiritdingiz")
ab_sonlar(a, b)

8
a = int(input("a son kiriting: "))
b = int(input("b son kiriting: "))
if a < b:
    def ab_sonlar(a, b):
        suum = 1
        for i in range(a, b):
            suum = suum *i
            print(suum)
else:
    print("xato son kiritdingiz")
ab_sonlar(a, b)

9
a = int(input("a son kiriting: "))
b = int(input("b son kiriting: "))
if a < b:
    def ab_sonlar(a, b):
        suum = 0
        for i in range(a, b):
            suum = (i**2)+suum
            print(suum)
else:
    print("xato son kiritdingiz")
ab_sonlar(a, b)

10
n = int(input("n butun sonini kiritin: "))
def nu(n):

    suum = 0
    for i in range(1, n):
        suum = 1/i+suum
        print(suum)
nu(n)

11
n = int(input("n butun sonini kiritin: "))
def nu(n):
    yigindi = 0
    suum = 0
    for i in range(1, 2*n+2):
        z = (n+suum)**2
        suum = i
        yigindi = z+yigindi
        print(yigindi)
nu(n)

12
n = int(input("n butun sonini kiritin: "))
def nu(n):
    kopaytma = 1
    for i in range(1, n+1):
        yigindi = (i+10)/10 *kopaytma
        print(kopaytma)
nu(n)

13
n = int(input("n butun sonini kiritin: "))
def nu(n):
    yigindi = 0
    for i in range(1, n*2, 2):
        yigindi = yigindi + (i+10)/10
        yigindi = yigindi - (i+11)/10
        print(yigindi)
nu(n)

14
n = int(input("n butun sonini kiritin: "))
def nu(n):
    yigindi = 0
    suum = 0
    for i in range(1, 2*n+1):
        
        print(yigindi)

15
a = int(input("a son kiriting: "))
n = int(input("n son kiriting: "))
def nk (a, n):
    yigindi = 0
    
    for i in range(1, n+1):
        yigindi = a**i
        print(a, "ning", i, "inchi darajasi", yigindi, "ga teng")

nk(a, n)

16
a = int(input("a son kiriting: "))
n = int(input("n son kiriting: "))
def nk (a, n):
    yigindi = 0
    
    for i in range(1, n+1):
        yigindi = a**i
        print(a, "ning", i, "inchi darajasi", yigindi, "ga teng")

nk(a, n)

17
a = int(input("a son kiriting: "))
n = int(input("n son kiriting: "))
def nk (a, n):
    yigindi = 0
    suuum = 1
    for i in range(1, n+1):
        yigindi = a**i
        suuum = suuum + yigindi
        print(a, "ning", i, "inchi darajasi", yigindi, "ga teng")
        print(f"yigindi {suuum}, ga teng")

nk(a, n)

18
a = int(input("a son kiriting: "))
n = int(input("n son kiriting: "))
def nk (a, n):
    yigindi = 0
    for i in range(n+1):
        yigindi =+ (-a)**i
        print(f" {yigindi}, ga teng")
nk(a, n)

19
n = int(input("n son kiriting: "))
def faktar(n):
    summ = 1
    for i in range(1, n+1):
        summ=i * summ
        print(summ)
faktar(n)

20
n = int(input("n son kiriting: "))
def faktar(n):
    summ = 1
    for i in range(1, n+1):
        kopaytma = 1
        yigindi = 0
        for j in range(1, i+1):
            kopaytma = j* kopaytma
            yigindi = kopaytma + yigindi
            print(f"{j}fatoriali yigindisi {yigindi}, ga teng")
        
        print()
faktar(n)
'''


#While============================================================================================================================
'''
s = int(input("summani kiriting: "))
p = int(input("foizni kiriting: "))
i = 0
while s <= 2 * s:
    s +=s+s*p/100
    i += 1
print(i)

16
a = 10
f = int(input("yugurish foizini kiriting"))
k = 1
while a < 200:
    a = a + a * f/100
    k += 1
print(k, a)

17
print("n > m")
n = int(input("n sonini kiriting"))
m = int(input("m sonini kiriting"))
z = m
if n > m:
    butun = 1
    while m < n:
        butun += 1
        m += z 
    print(butun, "butun", n-(z*butun), "qoldiq")


19
n = int(input("Sonni kiriting (n > 0): "))
y = 0
s = 0
while n > 0:
    raqam = n % 10
    y += raqam
    s += 1
    n = n // 10
print(f"Raqamlar yig'indisi: {y}")
print(f"Raqamlar soni: {s}")
'''




























































