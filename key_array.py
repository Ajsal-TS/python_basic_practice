
def groupById(users):
   return [{i["id"]:i} for i in users]

users = [{"id": 'john', "name": "John Smith", "age": 20},
  {"id": 'ann', "name": "Ann Smith", "age": 24},
  {"id": 'pete', "name": "Pete Peterson", "age": 31},
]
usersById = groupById(users)
print(usersById)
