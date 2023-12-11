"""To print the value of the dictionary between the a and b input given and the key must be arranged in the ascending order"""


def funct(s:dict,a:int,b:int,new={}):
    new={eval(j):eval(i) for j,i in s.items() if eval(i)>=a and eval(i)<=b}
    print(new)
    return {i:new[i] for i in sorted(new)}
    

    
dicts={"1":"2","4":"34","23":"1","254":"45","2":"30","6":"3"}
print(funct(dicts,1,20))