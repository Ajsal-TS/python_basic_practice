# def camelize(string:str):
#     return string.split("-")[:1][0]+"".join([i.capitalize() for i in string.split("-")[1:]])




def camelize(string:str):
    return string.casefold().split("-")[0]+"".join(string.title().split("-")[1:])
    # return string.split("-")[0]+"".join([i.capitalize() for i in string.split("-")[1:]])
    


print(camelize("background-color") == 'backgroundColor')
print(camelize("list-style-image") == 'listStyleImage')
print(camelize("-webkit-transition") == 'WebkitTransition')

# camelize("background-color")
# camelize("-webkit-transition")
