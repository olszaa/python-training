#!/usr/bin/python

_num1,_num2,_num3 = 4,5,3
# Example forif-elif-else statement 
if _num1 > _num2 and _num1 > _num3 :
    _max = "num1"
elif _num2 > _num3 :
    _max = "num2"
else:
    _max = "num3"
print("{0} as the greatest number ".format(_max))

# Example forif-elif-else statement  on one line
_max = "num1" if _num1 > _num2 and _num1 > _num3 else "num2" if _num2 > _num3  else "num3"
print("{0} as the greatest number ".format(_max))



# Example forif-elif-else statement 
if _num1 < _num2 and _num1 < _num3 :
    _min = "num1"
elif _num2 < _num3 :
    _min = "num2"
else:
    _min = "num3"
print("{0} as the less number".format(_min))

# Example forif-elif-else statement  on one line
_min = "num1" if _num1 < _num2 and _num1 < _num3 else "num2" if _num2 < _num3  else "num3"
print("{0} as the less number".format(_min))