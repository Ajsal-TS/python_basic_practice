
def uppers(func):
    def wrapper(*args):
        arr=[]
        print(args[0])
        [arr.append(i.capitalize()) for i in args[0]]
        arr=func(arr)
        return arr
    return wrapper


@uppers
def joining(word):
    k=" ".join(i for i in word)
    return k
word=["Hello","Hey","where"]
# s= {"a":1,"b":2,"c":3,"d":4}
print(joining(word))

# def print_message(message):
#     "Enclosong Function"
#     print("hi")
#     def message_sender():
#         "Nested Function"
#         print(message)
#     message_sender()

# print_message("Some random message")
