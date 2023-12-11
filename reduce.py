from collections import OrderedDict
from functools import reduce

"""Output confusing."""
# def sums(x):
#     s=0
#     print(x)
#     while s<x:
#         yield s
#         # print(1)
#         s+=1
# lst=[6,6,6,6,6,6,6,6]
# s=list(map(sums,lst))

d=OrderedDict({"b":1,"c":2,"g":2,"f":4,"l":3})
e=OrderedDict({"c":2,"g":2,"f":4,"b":1,"l":3})
# for i in d:
#     print(i)
print(d==e)
