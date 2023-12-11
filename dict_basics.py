# from collections import ChainMap


dicts={"a":{"a":1,"b":2},"b":{"b":2,"c":3},"c":{"d":4,"e":5}}
dict1={"a":1,"b":2,"c":3,"d":4}
dict2={"b":2,"c":3,"d":4,"e":5}
# print(dicts["a"]["b"])
# print(dicts["a"]["a"])

# s=ChainMap(dict1,dict2)
# print(s.maps)

# a,b,c={"ok"},["helo"],{}
# print(1 or 2 )
# print(1 and 2 and 3 and 1)
# print(a and b or c)
# print(a or b or c)
# print(a or c or b)

"""The is is the identity operator. When 2 variables are storing the same no then both are pointing to same object .(eg.a,b)
When list1 and 3 are assigned both point to different obj hence we get false when lst1 is lst2 while if lst1=lst3 and chekced
lst1 is lst3 returns true."""
lst1=[1,2,3]
lst2=[1,2,3]
a,b=10,15
print(a is b)
print(lst1 is lst2)

"""Prints based on the same sequence type"""
"""First2 elem are checked and then the 3rd elemnt get checked and founded 3<4 TRue"""
# print((1, 2, 3)<(1, 2, 4))
"""3 less than4 hence returns true without checking the next elem"""
# print([1, 2,3,4]< [1, 2, 4])
"""The first alph is checked and return the true. if same alph next alph will be looked."""
# print('ABC' < 'C' < 'Pascal' < 'Python')
""" 2elem are equal and 3rd elem present hence true"""
# print((1, 2)< (1, 2, -1))
# print((1, 2, 3)== (1.0, 2.0, 3.0))
"""3Rd elem is checked and found 3rd[2nd] not equal."""
# print((1, 2, ('aabc', 'ab')) < (1, 2, ('aabc', 'ca'), 4))
"""The alphh are checkd and third elem contain 1 alph more compared other alph are equal."""
# print("Ab"<"pz"<"pza")
# for v in lst1:
#     print(v)
"""The 3rd eelem contains the single digit where as the third elem in right section contains the 3elem hence it is greater"""
# print([1,2,[3],4,5]>[1,2,[3,6,5]])


a,b= set("abcdefg"),set("efghijk")
print(a - b) 
print(a^b)
print(a or b)