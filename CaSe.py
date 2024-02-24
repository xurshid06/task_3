'''
import math
1
h1 = "Dushanba"
h2 = "seyshanba"
h3 = "chorshanba"
h4 = "payshanba"
h5 = "Juma"
h6 = "Shanba"
h7 = "Yakshanba"
a = int(input("son kiriting: "))
if a == 1:
    print(h1)
elif a == 2:
    print(h2)
elif a == 3:
    print(h3)
elif a == 4:
    print(h4)
elif a == 5:
    print(h5)
elif a == 6:
    print(h6)
elif a == 7:
    print(h7)
else:
    print('hafta kunining sonini noto\'g\'ri kiritdingiz')

2
b1 = "Yomon"
b2 = "Qoniqarsiz"
b3 = "Qoniqarli"
b4 = "Yaxshi"
b5 = "A'lo"
a = int(input("Bahoni kiriting 1-5 gacha"))
if 1 == a:
    print(b1)
elif 2 == a:
    print(b2)
elif 3 == a:
    print(b3)
elif 4 == a:
    print(b4)
elif 5 == a:
    print(b5)
else:
    print("hato baho berdingiz")

3
o1 = "Yanvar"
o2 = "Fevral"
o3 = "Mart"
o4 = "Aprel"
o5 = "May"
o6 = "Iyun"
o7 = "Iyul"
o8 = "Avgust"
o9 = "Sentyabr"
o10 = "Oktyabr"
o11 = "Noyabr"
o12 = "Dekabr"
a = int(input("Nechanchi oyni izlayapsiz: "))
if a == 1:
    print(o1)
elif a ==2:
    print(o2)
elif a == 3:
    print(o3)
elif a == 4:
    print(o4)
elif a == 5:
    print(o5)
elif a == 6:
    print(o6)
elif a == 7:
    print(o7)
elif a == 8:
    print(o8)
elif a == 9:
    print(o9)
elif a == 10:
    print(o10)
elif a == 11:
    print(o11)
elif a == 12:
    print(o12)
else:
    print("oyni tartibi xato")

4
o1 = 31
o2 = 28
o3 = 31
o4 = 30
o5 = 31
o6 = 30
o7 = 31
o8 = 31
o9 = 30
o10 = 31
o11 = 30
o12 = 31
a = int(input("oyni tartib raqamini kiriting, men necha kun borligini korsataman: "))
if a == 1:
    print(o1, "kun bor")
elif a ==2:
    print(o2, "kun bor")
elif a == 3:
    print(o3, "kun bor")
elif a == 4:
    print(o4, "kun bor")
elif a == 5:
    print(o5, "kun bor")
elif a == 6:
    print(o6, "kun bor")
elif a == 7:
    print(o7, "kun bor")
elif a == 8:
    print(o8, "kun bor")
elif a == 9:
    print(o9, "kun bor")
elif a == 10:
    print(o10, "kun bor")
elif a == 11:
    print(o11, "kun bor")
elif a == 12:
    print(o12, "kun bor")
else:
    print("oyni tartibi xato")


5
a = 15
b = 5
print("1-qo'shish \t 2- ayirish \t 3-bo'lish \t 4- ko'oaytirish")
c = int(input("A =15, B = 5  qaysi amalni bajarishni tanlang: ")) 


if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a/b)
elif c == 4:
    print(a*b)
else:
    print("Bunday amal kiritilmagan!!!")

6
print("1-ditsimetr, 2-kilometr, 3-millimetr, 4-santimetr")
b = int(input("Birlikka qiymat bering, va u qiymatni metrda aniqlaymiz: "))
if b == 1:
    print("1-ditsimetr teng 0.1 metrga")
elif b == 2:
    print("1-kilometr teng 1000 metrga")
elif b == 3:
    print("1-millimetr teng 0.001 metrga teng")
elif b == 4:
    print("1 santimetr teng 0.01 metrga teng")

7
print("1-kilogram, 2-milligram, 3-gram, 4-tonna, 5-sentner")
a = int(input("qiymatni kiriting: "))
if a == 1 :
    print('1kilogram 1 kilogramga teng')
elif a == 2:
    print('2-milligram 0.0001 kilogramga teng')
elif a == 3:
    print("3-gram 0.003 kilogramga teng")
elif a == 4:
    print("4 tonna 4000kilogramga teng")
elif a == 5:
    print("5-sentner 500 kilogram")
else:
    print("bu qiymat topilmadi")

8
d = int(input("kunni belgilang: "))
a = int(input("oyni belgilang: "))
o1 = "Yanvar"
o2 = "Fevral"
o3 = "Mart"
o4 = "Aprel"
o5 = "May"
o6 = "Iyun"
o7 = "Iyul"
o8 = "Avgust"
o9 = "Sentyabr"
o10 = "Oktyabr"
o11 = "Noyabr"
o12 = "Dekabr"
if a == 1 and d < 31:
    print(d, o1)
elif a ==2 and d < 29:
    print(d, o2)
elif a == 3 and d < 31:
    print(d, o3)
elif a == 4 and d < 30:
    print(d, o4)
elif a == 5 and d < 31:
    print(d, o5)
elif a == 6 and d < 30:
    print(d, o6)
elif a == 7 and d < 31:
    print(d, o7)
elif a == 8 and d < 31:
    print(d, o8)
elif a == 9 and d < 30:
    print(d, o9)
elif a == 10 and d < 31:
    print(d, o10)
elif a == 11 and d < 30:
    print(d, o11)
elif a == 12 and d < 31:
    print(d, o12)
else:
    print("oyni tartibi xato")

9
b = int(input("kunni belgilang: "))
d = b+1
a = int(input("oyni belgilang: "))
o1 = "Yanvar"
o2 = "Fevral"
o3 = "Mart"
o4 = "Aprel"
o5 = "May"
o6 = "Iyun"
o7 = "Iyul"
o8 = "Avgust"
o9 = "Sentyabr"
o10 = "Oktyabr"
o11 = "Noyabr"
o12 = "Dekabr"
if a == 1 and d < 31:
    print("Keyingi kun ", d+1, o1)
elif a == 1 and d == 32:
    print("Keyingi kun ", 1, o2)
    
elif a ==2 and d < 29:
    print("Keyingi kun ", d+1, o2)
elif a == 2 and d == 30:
    print("Keyingi kun ", 1, o3)
    
elif a == 3 and d < 31:
    print("Keyingi kun ", d+1, o3)
elif a == 3 and d == 32:
    print("Keyingi kun ", 1, o4)
    
elif a == 4 and d < 30:
    print("Keyingi kun ", d+1, o4)
elif a == 4 and d == 31:
    print("Keyingi kun ", 1, o5)
    
elif a == 5 and d < 31:
    print("Keyingi kun ", d+1, o5)
elif a == 5 and d == 32:
    print("Keyingi kun ", 1, o6)
    
elif a == 6 and d < 30:
    print("Keyingi kun ", d+1, o6)
elif a == 6 and d == 31:
    print("Keyingi kun ", 1, o7)
    
elif a == 7 and d < 31:
    print("Keyingi kun ", d+1, o7)
elif a == 7 and d == 32:
    print("Keyingi kun ", 1, o8)
    
elif a == 8 and d < 31:
    print("Keyingi kun ", d+1, o8)
elif a == 8 and d == 32:
    print("Keyingi kun ", 1, o9)
    
elif a == 9 and d < 30:
    print("Keyingi kun ", d+1, o9)
elif a == 9 and d == 30:
    print("Keyingi kun ", 1, o10)
    
elif a == 10 and d < 31:
    print("Keyingi kun ", d+1, o10)
elif a == 10 and d == 32:
    print("Keyingi kun ", d+1, o11)
    
elif a == 11 and d < 30:
    print("Keyingi kun ", d+1, o11)
elif a == 11 and d == 31:
    print("Keyingi kun ", 1, o12)
    
elif a == 12 and d < 31:
    print("Keyingi kun ", d+1, o12)
elif a == 12 and d == 32:
    print("Keyingi kun ", 1, o1)
else:
    print("oyni tartibi xato")

10
o0, o1, o2 = "oldiga buril", "chapga buril", "o'nga buril" #komanda

s, j, sh, g = "shimolga", "janubga", "sharqqa", "g'arbga" #yonalish

print("3 ta komanda mavjud : 0 = oldiga, 1 = chapga, 2 = o'nga,")
print("4 ta yo'nalish mavjud: s = shimol, j = janub,  sh = sharq, g = g'arb")
b = int(input("kamandani kiriting: "))
a = input("yo'nalishni kiriting: ")
if b == 0:
    print(o0)
elif b == 1:
    print(o1)
elif b == 2:
    print(o2)
else:
    print("kamanda xato kiritildi.")
if a == "j":
    print(j)
elif a == "s":
    print(s)
elif a == "sh":
    print(sh)
elif a == "g":
    print(g)
else:
    print("yo'nalish xato kiritildi")

11
o0, o1, o2 = "o'nga buril", "chapga buril", "180 c burilish" #komanda

s, j, sh, g = "shimolga", "janubga", "sharqqa", "g'arbga" #yonalish

print("3 ta komanda mavjud : 0 = o'nga buril, 1 = chapga buril, 2 = 180 c burilish,")
print("4 ta yo'nalish mavjud: s = shimol, j = janub,  sh = sharq, g = g'arb")
b = int(input("kamandani kiriting: "))
a = input("yo'nalishni kiriting: ")
if b == 0:
    print(o0)
elif b == 1:
    print(o1)
elif b == 2:
    print(o2)
else:
    print("kamanda xato kiritildi.")
if a == "j":
    print(j)
elif a == "s":
    print(s)
elif a == "sh":
    print(sh)
elif a == "g":
    print(g)
else:
    print("yo'nalish xato kiritildi")

12
print("doiraning R, D, L yoki S larini birini kiriting qolganlarini topib beradi!")
print("1-radius R, 2-diametri D, 3-uzunligi L, 4-yuzasi S.")
a = int(input(" Yuqoridagi kamandalardan birini kiriting: "))
b = int(input("Qiymatni kiriting: "))
p = 3.14
if a == 1:
    print("D=", 2*b)
    print("L=", 2*3.14*b)
    print("S=", p*b**2)
elif a == 2:
    print("R=", b/2)
    print("L=", 2 * 3.14 * b)
    print("S=", p * b ** 2)
elif a == 3:
    print("R=", b/(2*p))
    print("D=", (b/(2*p))*2)
    print("S=", p *(b / (2 * p) ** 2))
elif a == 4:
    print("R=", math.sqrt(b/p))
    print("D=", (math.sqrt(b/p))*2)
    print("L=", 2*p*(math.sqrt(b/p)))

13
print("teng yonli uchburchakning a, c, h yoki S laridan birini kiriting qolganlarini topib beradi!")
print("1-katet 'a', 2-gipotenuza 'c', 3-gipotenuzaga tushurilgan balandlik 'h', 4-yuzasi 'S'")
a = int(input(" Yuqoridagi kamandalardan birini kiriting: "))
b = int(input("Qiymatni kiriting: "))
p = 3.14
if a == 1:
    print("c=", b*math.sqrt(2))
    print("h=", (b*math.sqrt(2))/2)
    print("S=", (b*math.sqrt(2)*((b*math.sqrt(2))/2))/2)
elif a == 2:
    print("a=", math.sqrt(b*2))
    print("h=", b/2)
    print("S=", (b*(b/2))/2)
elif a == 3:
    print("c=", b/2)
    print("a=", math.sqrt(b*2))
    print("S=", ((b*2)*b)/2)
# yuza berilganda qolganlarni topolmadim
'''
















































    
