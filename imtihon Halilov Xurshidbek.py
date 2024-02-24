
1
a = {1, 45, 78, 4}
b = {7, 4, 78, 1}
a.update(b)
print(min(a))

2
a = "Python 22 django3sndsiH20KNK34"
lis = []
for i in a:
    if i.isdigit():
        lis.append(int(i))
print(lis,sum(lis))

3
a = "Assalom"
a = a.lower()
lis = []
for i in a:
    if i not in lis:
        lis.append(i)
print(lis, len(lis), "ta harfdan foydalangan")

4
n = int(input("son kiriting: "))
dic = {}
for i in range(1, n+1):
    dic[i] = i ** 2
print(dic)

5
a = 10,20,3,0,2,5
b = 4,9,8,10,0, 2
a = set(a)
b = set(b)
c = a.intersection(b)
print(c)
