'''
lis = [1, 841, 621, 6, 32, 84 ,95, 74, 54, 55, 63, 95, 84, 71, 41]
lis2 = []
for i in lis:
    if i % 2 == 1:
        lis2.append(i)
lis2.sort(reverse = True)
print(lis2)

2
lis = [ 1, 3, 15, 17, 30, 37, 67, 4, 5, 99, 85, 71, 79, 97, 45, 85, 63, 45]
tub = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
tub2 = []
for i in lis:
    for j in tub:
        if i == j:
            tub2.append(i)
            lis.remove(i)
print(lis, "tub bo'lmagan sonlar")
print(tub2, "tub sonlar")

3
meva = ["anor", "olma", "banan", "uzum"]
m = input("meva kiriting: ")

for i in meva:
    if m != i:
        meva.append(m)

print(meva)

4
lis = [ 1, 3, 15, 17, 30, 37, 67, 4, 5, 99, 85, 71, 79, 97, 45, 85, 63, 45]
lis.sort()
a = len(lis)
orta = round(a/2)
print(lis[orta])

5
lis = [ 7, 3, 15, 17, 30, 37, 67, 4, 5, 99, 85, 71, 79, 97, 45, 85, 63, 45]
lis.sort()
kopaytma = lis[0] * lis[-1]
print(kopaytma)

6
meva = ["anor", "olma", "banan", "uzum"]
b = []
for i in meva:
   j = reversed(i)
   b.append(j)
b.sort()

7
lis1 = [ 7, 3, 15, 17, 30, 37, 67, 4, 5, 99, 85, 71, 79, 97, 45, 85, 63, 45]
lis2 = [89, 45 ,99, 97, 74, 45, 47, 45, 85, 30, 1, 6, 8, 47]
lis3 = []
for i in lis1:
    for j in lis2:
        if i == j:
            lis3.append(i)

print(lis3)

8
lis = ["anor", "olma", "banan", "uzum", "assalom", "son"]
for i in meva:
    a = 0
    for j in i:
        if j == "a":
            a = a+1
    if a == 2:
        meva.remove(i)
print(lis)            

9
lis1 = [1, 1, 3, 4, 4, 5, 6, 7]
lis2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
sum1 = 0
sum2 = 0
for i in lis1:
    sum1 = sum1 + i
for j in lis2:
    sum2 = sum2 + j

print((sum1+sum2)/(len(lis1)+len(lis2)))

10

lis1 = [1, 3, 5, 7, 9, 10]
lis2 = [2, 4, 6, 8]
lis1 [-1] = lis2
print(lis1)
'''




















        
        

