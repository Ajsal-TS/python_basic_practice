def getAverageAge(arr):
    return sum(i["age"] for i in arr)/len(arr)


john = { "name": "John", "age": 25 }
pete = { "name": "Pete", "age": 30 }
mary = { "name": "Mary", "age": 29 }

arr = [ john, pete, mary ]

print( getAverageAge(arr) )