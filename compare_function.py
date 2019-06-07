#!/usr/bin/python

print("Welcome Siwadon Chanaboon")

def compare(_num1, _num2, _num3):
    _max = ""
    _min = ""
    if _num1 > _num2 and _num1 > _num3 :
        _max = "num1"
    elif _num2 > _num3 :
        _max = "num2"
    else:
        _max = "num3"
    if _num1 < _num2 and _num1 < _num3 :
        _min = "num1"
    elif _num2 < _num3 :
        _min = "num2"
    else:
        _min = "num3"
    
    return (_max ,_min)

num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
num3 = int(input("Enter num3 :"))

#print("{0} as the greatest number \n{1} as the less number".format(compare(num1,num2,num3)[0],compare(num1,num2,num3)[1]))

mylist = compare(num1,num2,num3)
print("{0} as the greatest number \n{1} as the less number".format(mylist[0],mylist[1]))




