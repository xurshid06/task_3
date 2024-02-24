'''
my = {
    "name" : "",
    "age" : 23,
    "city" : "Buxoro",
    "malumoti" : "oliy",
    "tel" : 9995324896
    }
print(len(my))
print(my["name"])
a = my.get("city")
print(a)
print(my.keys())
b = my.values()
print(b)
allitems = my.items()
print(allitems)


my = {
    "name" : "john",
    "age" : 23,
    "city" : "Buxoro",
    "malumoti" : "oliy",
    "tel" : 9995324896
    }
my["name"] = "Jack"
#print(my.items())
my.update({"name" : "Moly"})
print(my)
my3 = dict(my)
my ["hobby"] = "compyuter game"
print(my)
my.pop("age")
print(my)
my.popitem()
print(my)
my2 = my.copy()
del my ["city"]
print(my)
my.clear()
print(my)
print(my2)
print(my3)

print(my3.get("name1"))

for i in my3.keys():
    print(i)

for i in my3.values():
    print(i)


for i,j in my3.items():
    print(i, "keys")
    print(j, "names")

D = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Cod'},
    'emp4': {'name': 'Hun', 'job': 'Dev'},
    'emp5': {'name': 'Jin', 'job': 'Hr'},
    'emp6': {'name': 'Pin', 'job': 'Mgr'},
    'emp7': {'name': 'Sam', 'job': 'Mgr'},
    'emp8': {'name': 'Bob', 'job': 'Dev'},
}
'''
sampleDict = {
    "class" : {"student" : {"name" : "Mike", "marks": {"Physics" : "70", "history" : "80"}}}

    }

for i in sampleDict.values():
    for j in i.values():

        for k in j.values():
            a = k.
            print(a)
                
           
        
        
        
        
            





































