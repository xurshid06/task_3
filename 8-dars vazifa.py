'''
1
dic1={
    "a":10,
    "b":20,
    "c":5,
    "d":80,
    "e":4,
    "f":15
    }
ds = sorted(dic1.values())
print(ds)

2
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic = {}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)
print(dic)

3
n = int(input("n sonini kiriting"))
res = {}
for i in range(1, n+1):
    res[i] = i ** 2
    
print(res)

4
dic1={
    "a":10,
    "b":20,
    "c":5,
    "d":80,
    "e":4,
    "f":15
    }
res = 0
for i in dic1.values():
    res = i + res
print(res)

5
dic1={
    "a":10,
    "b":20,
    "c":5,
    "d":80,
    "e":4,
    "f":15
    }
katta = 1
for i in dic1.values():
    if i > katta:
        katta = i
print(katta)

6
dic1={
    "a":10,
    "b":20,
    "c":5,
    "d":80,
    "e":4,
    "f":15
    }

kichik = dic1.get("a")
for i in dic1.values():
    if i < kichik:
        kichik = i
print(kichik)

7
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
res = {}
for i, j in d1.items():
    if i in d2:
        res[i] = d1.get(i) + d2.get(i)
        
    else:
        res[i] = j
for k, l in d2.items():
    if k not in d1:
        res[k] = l
print(res)

8
a = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
res = {}
for i in a:
    for k in i.values():
        if k not in res:
            res = k
            print(res, end = ", ")

9
soz = input("soz kiriting: ")
res = {}
for i in soz:
    soni = soz.count(i)
    res[i] = soni
print(res)

10
a =  "mexanizasiyalashtirilganmi"
res = {}
for i in a:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
so = sorted(res.items())
print(max(so), min(so))  #shuni print iqlishi teskari bo'lyapti shunga tushunmadim!

11
dic = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
    'д': 'd', 'е': 'e', 'ё': 'y', 'ж': 'o',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
    'л': 'l','м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'h', 'ш': 'sh', 'щ': "sh'", 'ъ': "'",
    'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu',
    'я': 'ya'
       }
lis = []
soz = input("krilcha so'z yozing: ")
for i in soz:
    lis  = dic.get(i)
    print(lis, end = "")
12
dic = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
    'д': 'd', 'е': 'e', 'ё': 'y', 'ж': 'o',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
    'л': 'l','м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'h', 'ш': 'sh', 'щ': "sh'", 'ъ': "'",
    'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu',
    'я': 'ya'
       }
dic2 = {}
for i, j in dic.items():
    dic2[j] = i   # dic lug'atini key larini value ga value larini keylarga almashtirdik
    
lis = []
soz = input("lotincha so'z yozing: ")
for i in soz:
    lis = dic2.get(i)
    print(lis, end = "")
'''    

    
    
    
    
    
    
        
   



































