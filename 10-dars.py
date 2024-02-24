'''sett = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
sett.add("maline")
#sett.clear()
sercop = sett.copy()
sett.difference_update()
sett.discard("cherry")
sett.intersection_update(set2)
print(sett)

def fin (x):
    if len(x) >= 1:
        if type(x) == tuple or type(x) == set:
            return True
        elif type(x) == list or type(x) == dict:
            return False
        else:
            return 'Error'
    else:
        return "Error because, this is free!"
x = 
print(fin(x))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
s = set1.symmetric_difference_update(set2)
print(s)
