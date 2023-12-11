# def filterRange(arr:list,a,b):
#     # return list(filter(lambda c:c>=a and c<=b,arr))
#     # print(type([arr.remove(c) for c in arr if c>=b or c<=a]))
#     [arr.remove(c) for c in arr if c>=b or c<=a]
#     return arr
# arr = [5, 3, 8, 1]
# arr=filterRange(arr, 1, 4)
# print(arr)









def sortByProperty(users, property):
    return sorted(users, key=lambda x:x[property])

# Test Case
users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
print(sortByProperty(users, 'age'))