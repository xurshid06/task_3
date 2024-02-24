'''
1
a = [1, 1, 3, 4, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
c = 0
for i in a:
    c += i
for j in b:
    c += j
res = c / (len(a) + len(b))
print(res)

2
lis = [1, 4, 3, 9]
rm = 'RM'
res = []
for i in lis:
    z = str(i)
    res.append(rm + z)
print(res)

3
lis = [[1,2,3],[4,5,6,],[10,11,12],[7,8,9,]]
res = []
summ = 0
for i in lis:
    if sum(i) > summ:
        summ = sum(i)
        res.clear()
        res.append(i)
print(res)

4
a = [1,'abc',3,1.2,4,'xyz',5,'pqr',7,-5,-12.22]
sr = 0
for i in a:
    if type(i) == int:
        sr += 1

print(sr)

5
a = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
res = 0
for i in a:
    b = a.count(i)
    if b > res:
        res = b
        print(i, "-->", res, "marta takrorlandi")

6
a = [1,2,10]
index = len(a) -1
a [index] += 1
while a[index] == 10 and index > 0:
    a[index] == 0
    index -= 1
    a[index] += 1
print(a)

7
a = int(input("nechta son kiritmoqchisiz: "))
lis = []
for i in range(a):
    b = int(input(f"{i+1}, sonni kiriting: "))
    lis.append(b**2)
print(lis)

8
a = [1, 4, 3, 9]
b = ['chelsea', 'real', 'barca', 'MU']
lis = []
for i in range(len(a)):
    lis.append(b[i] + str(a[i]))
print(lis)

9
a = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(max(c))

10

a = 'sfb9wue8qfu5q2'
res = 0
for i in a:
    if i.isdigit():
        res += int(i)
print(res)    





















    
    
