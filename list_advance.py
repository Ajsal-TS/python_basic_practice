from collections import Counter
import time

"""To print the elements with the tuple having 1st and 2nd element combined with the third element."""
test_list = [[4, 5, 6,7], [2, 4, 5], [6, 7, 5]]
# print((len(test_list)-2))
d=[(i[j],i[len(i)-1]) for i in test_list for j in range(len(test_list)-1)]
# print(d)

"""To count the unique elements."""
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
s=Counter(input_list)
# print(len(s))

"""Print element having freq great than k"""
test_list,k= [4, 6, 4, 3, 3, 4, 3, 7, 8, 8,8],2
freq=[j for j,i in Counter(test_list).items() if i>k]
# print(freq)

"""To check whether all element inside the range."""
test_list = [4, 5, 6, 7, 3, 9]
i,j=3,10
# if all(i<=n<j for n in test_list):
    # print(True)
# else:
    # print(False)

"""To check 3 same consecutive element inside the list."""
lst=[4, 5, 5, 5, 3, 8,6,6,6]
lst2=[]
[lst2.append(lst[i]) for i in range(len(lst)-2) if lst[i]==lst[i+1] and lst[i]==lst[i+2]]
# print(lst2)

"""To print the team leader."""
lst=[1,2,5,2,5,21,6,8,3,6,2,8]
lst2=list(reversed([lst[i] for i in range(len(lst)-2,0,-1) if lst[i]>lst[i-1] and lst[i]>lst[i+1]]))
lst2.append(8)
print(lst2)