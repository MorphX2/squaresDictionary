import random

x = 1
intdict = { }
number_range = 10
while x <= number_range:
    key = x
    value = x
    intdict.update({key:value * value})
    x = x + 1

#for k, v in intdict.items():
#    print("{%d, %d}" % ( k, v ))

print(intdict)
