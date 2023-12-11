def sortByAge(arr:list):
    [arr.sort(i["age"]) for i in arr]

john = { "name": "John", "age": 25 }
pete = { "name": "Pete", "age": 30 }
mary = { "name": "Mary", "age": 28 }

arr = [ pete, john, mary ]
sortByAge(arr)

# // now: [john, mary, pete]
print(arr[0].name) # John
print(arr[1].name) # Mary
print(arr[2].name) # Pete