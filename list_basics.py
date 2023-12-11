"""To swap the elements of the list."""
lst1=[12, 35, 9, 56, 24]
lst1[0],lst1[len(lst1)-1]=lst1[len(lst1)-1],lst1[0]

"""To get the new list removing the empty elements."""
test_list = [5, 6, [], 3, [], [], 9, {}, {}]
new_list=[i for i in test_list if bool(i)]
# print(new_list)

"""To print the list  in key value pairs from the 2 list."""
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"] 
lenght=len(test_list)
lst2=[{key_list[0]:test_list[i],key_list[1]:test_list[i+1]} for i in range(0,lenght,2)]
# print(lst2)

"""To convert  the list of list of elements to the dictionary."""
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
dicts={(i[0],i[1]):(i[2],i[3]) for i in test_list }
# print(dicts)

# expected:
# the mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

"""To select the random element from a list."""
from random import choice
test_list = [[5, 5, 5], [2, 7, 6], [8, 6, 3]]
if not bool(test_list):
    print("enter the elements in the list.")
else:
    ch=[0,1,2]
    # print(test_list[choice(ch)][choice(ch)])

"""Find uncommonality in the list."""
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
reset=set(map(tuple,test_list1)).symmetric_difference(set(map(tuple,test_list2)))
# print(list(map(list, reset)))
# print(s.difference(m))

"""Chain mapes are used to compress the dictionary where chainmap(dict1,dict2).map 
gives the list of the combined dict1 and dict2 in a list while 
list(chainmap(dict1,dict2).keys()) helps to get the list of key and for getiing the
value (chainmap(dict1,dict2).values) helps to get the list of values."""

from collections import ChainMap
d1={1:2,2:3,4:5}
d2={2:3,4:5,5:6,6:7}
print(ChainMap(d1,d2))
maps_d=ChainMap(d1,d2)
print(maps_d.maps)
print(list(maps_d.keys()))
# print(list(maps_d.values())[0])

"""Deque have low time complexity O(1) where used to pop and append element to right and left of list.
deque(lst).append() default append to right and deque(lst).appendleft("") to appenf left .
similarly pop and popleft can be used."""

