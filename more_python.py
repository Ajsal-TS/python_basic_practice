"""To count the no of vowels."""
from collections import Counter
def countVowels(a):
    print(sum([j for i,j in Counter(a).items() if i in {"a","e","i","o","u","O","E","I","A","U"}]))

# Test Cases
countVowels("hello")  # Expected Output: 2
countVowels("python")  # Expected Output: 1
countVowels("HeLOoooOOOooooO")


"""To transform the matrix"""
def transposeMatrix(lst):
    print(list(zip(*lst)))
# Test Cases
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposeMatrix(matrix)  # Expected Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


"""Palindrome of the string"""
# def isPalindrome(a):
#     print(all(a[i]==a[int(len(a))-i-1] for i in range(int(len(a)/2))))
# # Test Cases
# isPalindrome("radar")  # Expected Output: True
# isPalindrome("python")  # Expected Output: False

"""Fatorial REcursion......f(0)--1 f(1)--1 f(2)--n*n-1   f(3)--n*n-1"""
from collections import Counter


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# factorial(5)

"""Common elemnt from2 list."""
# def listIntersection(lst1,lst2):
#     print(list(set(lst1)&set(lst2)))
# # Test Cases
# listIntersection([1, 2, 3, 4], [3, 4, 5, 6])  # Expected Output: [3, 4]
# listIntersection(['a', 'b', 'c'], ['b', 'c', 'd'])  # Expected Output: ['b', 'c']

# def areAnagrams(a,b):
#     print(Counter(a)==Counter(b))

# areAnagrams("listen", "silent")  # Expected Output: True
# areAnagrams("hello", "world")

"""Prime no upto n"""
# def getPrimes(n):
#     lst1=[i for i in range(2,n) if all(i%j!=0 for j in range(2,int(i/2)+1))]
#     print(lst1)

# getPrimes(10)  # Expected Output: [2, 3, 5, 7]
# getPrimes(20)  # Expected Output: [2, 3, 5, 7, 11, 13, 17, 19]

"""Reverse words in a string."""
# def reverseWords(s):
#     print(" ".join([i for i in s.split()[::-1]]))

# reverseWords("Hello World")  # Expected Output: "World Hello"
# reverseWords("Python is fun") # Expected Output: "fun is Python"

"""remove duplicates from the list while 
 preserving the order."""
from collections import OrderedDict
# def removeDuplicates(lst:list):
#     print(list(OrderedDict.fromkeys(lst)))
    

# # Test Cases
# removeDuplicates([1, 2, 2, 3, 4, 4, 5])  # Expected Output: [1, 2, 3, 4, 5]
# removeDuplicates(['a', 'b', 'a', 'c', 'b'])  # Expected Output: ['a', 'b', 'c']


""" compress string"""
# def compressString(d):
#     count,s=1,""
#     # print([s+f"{i}"+f"{k}" for i in d if k<(len(d)-1) if i!=d[k:=k+1]])
#     try:
#         for i in range(1,len(d)):
#             if d[i]==d[i-1]:
#                 count+=1
#             else:
#                 print(d[i])
#                 if count==1:
#                     s=s+d[i]
#                 else:
#                     s=s+d[i]+str(count)
#                 count=1
#         print(s)
#     except IndexError:
#         print(f"index out")
# # Test Cases
# compressString("aaabbbcc")  # Expected Output: "a3b3c2"
# compressString("abcde")  # Expected Output: "abcde"

"""Matrix multiplication."""
def matrixMultiplication(a,b):
    c=len(a)
    print([a[i][j]*b[j][i] for i in range(c) for j in range(c)])


# Test Cases
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
matrixMultiplication(matrix1, matrix2)  # Expected Output: [[19, 22], [43, 50]]


"""STring rotation"""

def isRotation(a,b):
    # print(all(i in b for i in a.split(a[len(a)-1])))
    if len(a)!=len(b):
        return False
    print(b in a+a)
# Test Cases
isRotation("abcd", "cdab")  # Expected Output: True
isRotation("hello", "world")  # Expected Output: False
isRotation("python", "thonpy")  # Expected Output: True
isRotation("abcde", "eabcd")  # Expected Output: True
isRotation("abc", "cab")  # Expected Output: True
isRotation("12345", "45123")  # Expected Output: True
isRotation("xyz", "zxy")  # Expected Output: True
isRotation("abc", "acb")  # Expected Output: False


# # Test Cases
# def chunkList(a,b):
#     print([a[i:i+b] for i in range(0,len(a),b)])
# chunkList([1, 2, 3, 4, 5, 6], 2)  # Expected Output: [[1, 2], [3, 4], [5, 6]]
# chunkList(['a', 'b', 'c', 'd'], 3)  # Expected Output: [['a', 'b', 'c'], ['d']]


# # # Test Cases

# # Test Cases
def rotateArray(a,b):
    print(a[-b:]+a[:len(a)-b])
rotateArray([1, 2, 3, 4, 5], 2)  # Expected Output: [4, 5, 1, 2, 3]
rotateArray(['a', 'b', 'c', 'd'], 3)  # Expected Output: ['b', 'c', 'd', 'a']



