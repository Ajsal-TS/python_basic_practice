john = { "name": "John", "surname": "Smith", id: 1 }
pete = { "name": "Pete", "surname": "Hunt", id: 2 }
mary = { "name": "Mary", "surname": "Key", id: 3 }

users = [ john, pete, mary ]

usersMapped = [{"fullName":i["name"]+i["surname"],"id":i[id]} for i in users]


# usersMapped = [
#   { "fullName": "John Smith", id: 1 },
#   { "fullName": "Pete Hunt", id: 2 },
#   { "fullName": "Mary Key", id: 3 }
# ]


print( usersMapped[0]["id"] )
print( usersMapped[0]["fullName"] ) 