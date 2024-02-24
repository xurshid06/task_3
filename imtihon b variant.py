variant b
1

res = 0
iss = []
qator1 = input("malumotlarni kiriting:")
qator2 = input("malumotlarni kiriting:")
malumotlar1 = qator1.split()
malumotlar2 = qator2.split()
if len(malumotlar1) != 2:
    print("malumotlarni boshqatdan kiriting")
if len(malumotlar2) != 2:
    print("malumotlarni boshqatdan kiriting")
if int(malumotlar1[0]) > res:
        iss.append(malumotlar1[1])
if int(malumotlar2[0]) > res:
        iss.clear()
        iss.append(malumotlar2[1])
print(iss)
2
a = "Heii5, mY N@m3 1S An9nym2u5SBd323f"
res = []
for i in a:
    if i.isupper():
        res.append(i)
print(res, len(res))
3
a = "145048207"
res = ""
for i in a:
    if i == "7":
        res += "4"
    elif i == "4":
        res += "7"
    else:
        res += (i)
print(res)
4
a = "Pythonforloop"
h = ""
s = 0
for i in a:
    count = a.count(i)
    if count > s:
        s = count
        h = i

print(h, s)
5
a = {5,4,7,8,1,9}
b = {1,5,0,20,7}
c = a.intersection(b)
tes = list(c)
tes.reverse()
print(tes)
