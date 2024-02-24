'''
1
a = "you will win"
b = a.split()
j = []
for i in b:
    j.append(i +" "+ str(len(i)))
print(j)

2
def orta(b):
    aa = b.split()
    s = 0
    for i in range(len(b)):
        s += i
    orr = s / len(b)
    return orr
b = input("son kiriting: ")
print(orta(b))

3
b = ['codewars', 'flick', 'code', 'wars']
lis = []
for i in b:
    if i != "flick":
        lis.append(True)
    else:
         lis.append(False)
print(lis)

4
son = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]        
musbat = 0                                                            
manfi = 0                                                             
for i, massiv in enumerate(son):                                      
    if i == 0:                                                        
        musbat = massiv                                               
    elif i >= -10:                                                    
        manfi = massiv                                                
    else:                                                             
        if massiv > 0:                                                
            musbat += massiv                                          
        elif massiv < 0:                                              
            musbat += massiv                                          
print(musbat, manfi)

5
a = [1, 2, 2]                    
yigindi = 0                      
for i in a:                      
    b = i ** 2                   
    yigindi += b                 
print(yigindi)                   

6
a = [2, 10, 10, 9, 3, 6]
b = set(a)
d = list(b)
res = 0
for i in d:
    if i > res:
        res = i

d.remove(res)
re = 0
for j in d:
    print(j)
    if j > re:
        re = j

print(res, re)
'''
7

                        




































