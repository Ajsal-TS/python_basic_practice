"""a=1,2..creates a tuple(1,2)...b=(3,4)..a+b=(1,2,3,4)
tups=(1)--str,tups*3--111,,tups=(1,)--tuple,,,tups*3---(1,1,1)
"""
"""1
   22
   333
   4444"""
# n=eval(input())
# for i in range(1,n+1):
    # print(f"{i}"*i)

"""1111
   222
   33
   4"""
# n=eval(input())
# s=n
# for i in range(1,n+1):
    # print(f"{i}"*s)
    # s-=1

"""1
   12
   123
   1234
   12345"""
# n=eval(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(f"{j+1}",end="")
#     print(" ")

"""55555
   4444
   333
   22
   1"""
# n=eval(input())
# for i in range(n,0,-1):
#     print(f"{i}"*i)


"""012345
   01234
   0123
   012
   01"""
# n=eval(input())
# for i in range(n,0,-1):
#     for j in range(0,i+1):
#         print(f"{j}",end="")
#     print("")


from functools import reduce


"""Reduce and the lambda functions in the python."""
# print(reduce(lambda x,y:x+y,lst1))
# print([(lambda i,j:(i+1,j+2))(i,j) for i in range(5) for j in range(2)]) 

# n=int(input())
# count=0
# for i in range(1,n+1):
#     s=0
#     while(s<2*i-1):
#         count+=1
#         s+=1
#         print(count, end=" ")

"""
1 

1 2 1 

1 2 3 2 1 

1 2 3 4 3 2 1 

1 2 3 4 5 4 3 2 1"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f"{j}",end="")
#     for j in range(i-1,0,-1):
#         print(f"{j}",end="")
#     print(" ")
    
"""
10 

10 8 

10 8 6 

10 8 6 4 

10 8 6 4 2
"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(0,i):
#         print(10-(2*j),end=" ")
#     print("")

"""walrus operator"""
# walrus eoperator can be used by the paranthesis around it and used for assignment operation (k:=k+1)
   #  inside the list compreension it is used by if statement that incrment and check the condition.

"""
            *   

           * *   

          * * *   

         * * * *   

        * * * * *
           
         * * * * 

          * * * 

           * * 

            *  """

# n=int(input())
# for i in range(n):
#     print(" "*(n-i),"* "*(i+1))
#     print(" ")
# for j in range(n-1,0,-1):
#     print(" "*(n-j+1),"* "*j)
#     print(" ")

"""
         1 

       1 2 

     1 2 3 

   1 2 3 4 

 1 2 3 4 5"""
# n=int(input())
# k=0
# for i in range(1,n+1):
#     print(" "*2*(n-i),end="")
#     for j in range(1,i+1):
#         print(f"{j}",end=" ")
#     print(" ")

