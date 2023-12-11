"""Fibnocci no"""
# def fib(n:int):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     # lst.append(0)
#     return fib(n-1)+ fib(n-2)

"""natural no sum"""
# def sum_nat(n):
#     if n==1 or n==0:
#         return 1
#     return n+sum_nat(n-1)


"""sum of the digits of input value."""
# def sum_digit(n:str,i):
#     print(i)
#     if n[i]==n[0]:
#         return int(n[0])
#     return int(n[i])+sum_digit(n,i-1)

# n=str(eval(input()))
# i=len(str(n))-1
# print(sum_digit(n ,i))

"""To print pattern without any loop.n,n-5,n-10,n-15...."""
# 16,11,6,1,-4,1,6,11,16, 16-n,,11-n-5,,6-n-5,,1-n-5,,-4-n-5,,
# lis.append((p16-(p11)-(p6)-(-4)))
def patt(n,lis:list,flag):
    lis.append(n)
    print(n,flag,lis)
    if n<0 :
        flag=1
        return lis
    elif n>lis[0]:
        return lis
    if flag==0:
        patt(n-5,lis,flag)
    if n==lis[0]:
        flag=1
    print(n,flag)
    if flag==1:
        s=lis[len(lis)-1]
        return patt(s+5,lis,flag=1)
    
n,s,lis=int(input()),0,[]
patt(n,lis=[],flag=0)
print(lis)