class calc():
    def __init__(self,a,b) -> None:
        self.methord={}
        self.a=a
        self.b=b
        self.methord["+"]=self.addition(self.a,self.b)
        self.methord["-"]=self.subraction(self.a,self.b)
        self.methord["*"]=self.multiple(self.a,self.b)
    def  choice(self,c):
        print(type(c))
        print(self.methord)
        return self.methord[c]
    def addition(self,a,b):
        print(self.choice("-"))
        return a+b
    def subraction(self,a,b):
        return a-b
    def multiple(self,a,b):
        return a*b
    
n=input()
""" '2 + 3 ' """
a,b,c=eval(n.split()[0]),eval(n.split()[2]),n.split()[1]
calculation=calc(a,b)
print(calculation.choice(c))