
john = { "name": "John", "age": 25 }
pete = { "name": "Pete", "age": 30 }
mary = { "name": "Mary", "age": 28 }

users = [ john, pete, mary ]

names = [i["name"] for i in users]

print( names ) # // John, Pete, Mary