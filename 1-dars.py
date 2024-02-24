import math
 #   1-dars

# 1-masala
'''
a = int(input('kvadratni tomonini kiriting: '))
print("P=", a*4)

# 2-masala

a = int(input('kvadratni tomonini kiriting: '))
print("S=", a**2)

# 3-masala

a = int(input('to\'rtburchakning b\'yini kiriting: '))
b = int(input('to\'rtburchakningenini kiriting: '))
Yuza = a*b
Perimetr = (a+b)*2
print('S=', Yuza, ' ', 'P=',Perimetr )


# 4-masala
d = int(input('aylananing diametrini kiriting: '))
pi = 3.14

print('L=', d*pi)

# 5-masala
a = int(input('kubning tomonini kiriting: '))
print('V=', a**3, ' ', 'S=', 6*a**2 )

# 6-masala
a = int(input('paralelopidedning 1-tomonini kiriting: '))
b = int(input('paralelopidedning 2-tomonini kiriting: '))
c = int(input('paralelopidedning 3-tomonini kiriting: '))
print('V=', a*b*c)
print('S=', 2*(a*b+b*c+c*a))

# 7-masala
r = int(input('doiraning radiusini kiriting: '))
pi=3.14
print('L=', 2*pi*r)
print('S=', pi*r**2)

# 8-masala
a = int(input('1-sonni kiriting: '))
b = int(input('2-sonni kiriting: '))
print('sonlarni o\'rta arifmetigi:', (a+b)/2)

# 9-masala
a = int(input('musbat sonni kiriting: '))
b = int(input('musbat bo\'lmagan 2-sonni kiriting: '))
result = math.sqrt(a*b)
print('sonlarni o\'rta geometrigi: ',result)

# 10-masala
a = int(input('0 dan katta 1-sonni kiriting: '))
b = int(input('0 dan katta 2-sonni kiriting: '))
print('sonlarning yig\'indisi: ', a+b)
print('sonlarni ko\'paytmasi: ', a*b)
print('1-sonnning kvadrati: ', a**2)
print('2-sonning kvadrati: ', b**2)

# 11-masala
a = int(input('0 dan katta 1-sonni kiriting: '))
b = int(input('0 dan katta 2-sonni kiriting: '))
print('sonlarning yig\'indisi: ', a+b)
print('sonlarni ko\'paytmasi: ', a*b)
print('1-sonnning moduli: ', abs(a))
print('2-sonning kvadrati: ', abs(b))

# 12-masala
a = int(input('uchburchakning 1-tomonini kiriting: '))
b = int(input('uchburchakning 2-tomonini kiriting: '))
g = a**2+b**2
gip = math.sqrt(g)
.
print("C= ", gip)
print("P= ", gip+a+b)

# 13-masala
r1 = int(input('katta aylananing radiusini kiriting: '))
r2 = int(input('kichik aylananing radiusini kiriting: '))
pi=3.14
s1 = pi*r1
s2 = pi*r2
s3 = pi*(r1-r2)
print("S1", s1)
print("S2", s2)
print("S3", s3)

# 14-masala
u = int(input('aylanani uzunligini kiriting: '))
pi = 3.14
r = l/(2*pi)
s = pi*r**2
print("R= ", r)
print("S= ", s)

# 15-masala
s = int(input('aylanani uzunligini kiriting: '))
pi = 3.14
r = math.sqrt(s/pi)              
u = 2*pi*r
print("R=", r)
print("S=", u)

# 16-masala
a = int(input('sonlar o\'qidagi x1 nuqtani kiriting: '))
b = int(input('sonlar o\'qidagi x2 nuqtani kiriting: '))
print('ular orasidagi masofa=', b-a, 'ga teng')

# 17-masala
a = int(input('sonlar o\'qidagi a nuqtani kiriting: '))
b = int(input('sonlar o\'qidagi b nuqtani kiriting: '))
c = int(input('sonlar o\'qidagi c nuqtani kiriting: '))
print('AC kesmani uzunligi=', c-a)
print('BC kesmani uzunligi=', c-b)
print('AC kesma va BC kesma  uzunligi yig\'indis =', (c-a)+(c-b))

# 18-masala
a = int(input('sonlar o\'qidagi a nuqtani kiriting: '))
b = int(input('sonlar o\'qidagi b nuqtani kiriting: '))
c = int(input('sonlar o\'qidagi c nuqtani kiriting. c nuqta a va b nuqtalar orasida joylashgan: '))
print('AC kesmani uzunligi=', c-a)
print('BC kesmani uzunligi=', b-c)
print('AC kesma va BC kesma  uzunligi ko\'paytmasi =', (c-a)*(b-c))
print('Agar javob musbat son bo\'lsa siz masala shartlarini to\'g\'ri bajargansiz')

# 19-masala
a = int(input('to\'g\'ri to\'rtburchakni a tomonini  kiriting: '))
b = int(input('to\'g\'ri to\'rtburchakni b tomonini kiriting: '))
print('P=', (a+b)*2)
print('S=', a*b)

# 22-masala
a = int(input('a  kiriting: '))
b = int(input('b  kiriting: '))
c = a
a = b
b = c
print('a=',a, 'b=', b)
print('a va b qiymatlar almashdi')

# 23-masala
a = int(input('a  kiriting: '))
b = int(input('b  kiriting: '))
c = int(input('c  kiriting: '))
d = a
a = b
b = c
c = d
print('a=',a, 'b=', b, 'c=', c)

# 24-masala

d = a
a = c
c = b 
b = d
print('a=',a, 'b=', b, 'c=', c)

# 25-masala
x = int(input('x  kiriting: '))
y = (3*x**3)-(6*x**2)-7
print(y)

# 26-masala
x = int(input('x  kiriting: '))
y = (4*(x-3)**6)-(7*(x-3)**3)+2
print(y)

# 27-masala
a = int(input('a  kiriting: '))
print('A ning ikkinchi darajasi=', a**2)
print('A ning to\'rtinchi darajasi=', a**4)
print('A ning sakkizinchi darajasi=', a**8)

# 28-massala
a = int(input('a  kiriting: '))
print('A ning ikkinchi darajasi=', a**2)
print('A ning uchinchi darajasi=', a**3)
print('A ning beshinchi darajasi=', a**5)
print('A ning o\'ninchi  darajasi=', a**10)
print('A ning o\'nbeshinchi darajasi=', a**15)

# 29-massala
a = int(input('alfa burchakni darajasini  kiriting: '))
pi = 3.14
print('Radyan= ', a*(pi/180))

# 30-masala
a = int(input('radianni  kiriting: '))
pi = 3.14 
print('Daraja= ', a*(180/pi))

# 31-masala
a = int(input('Farengeyt haroratni  kiriting: '))
c = (a-32)*(5/9)
print('Tc=', c)

# 32-masala
c = int(input('Selsiyda haroratni  kiriting: '))
f = c*(9/5)+32
print('Tf=', f)

# 33-masala
x = int(input('shokoladni 1 kilosini narxini kiriting: '))
y = int(input('kanfetni 1 kilosini narxini kiriting: '))
print('shokolatning kilosi: ', x, 'turadi')
print('kanfetni kilosi: ', y, 'turadi')

# 34-masala
x = int(input('shokoladni 1 kilosini narxini kiriting: '))
y = int(input('kanfetni 1 kilosini narxini kiriting: '))
print('shokolatning kilosi konfetdan', x-y, 'qimmat turadi')
'''
# 35-masala

v = int(input('Qayiqni tezligini   kiriting(km/s): '))
u = int(input('Oqimni tezligini  kiriting(km/s): '))
t1 = int(input('Qayiqni daryo oqimi bo\'yicha harakatlanish vaqtini  kiriting: '))
t2 = int(input('Qayiqni oqimga qarshi harakatlanish vaqtini kiriting: '))
print('Qayiq yurgan yo\'l', v )




# 37-masala
v1 = int(input('1-avtomobil tezligini   kiriting(km/s): '))
v = int(input('2-avtomobil tezligini   kiriting(km/s): '))

 = int(input('Oqimni tezligini  kiriting(km/s): '))
t1 = int(input('Qayiqni daryo oqimi bo\'yicha harakatlanish vaqtini  kiriting: '))
t2 = int(input('Qayiqni oqimga qarshi harakatlanish vaqtini kiriting: '))





























