# class Calculator():
#     def __init__(self)->None:
#         self.methord={}
#     def addMethod(self,name,func):
#         self.methord[name]=func
#     def calculate(self,exp:str,):
#         try:
#             return self.methord[exp.split(" ")[1]](eval(exp.split(" ")[0]),eval(exp.split(" ")[2]))
#         except:
#             return ("Provide with the correct input")



from functools import reduce


class Calculator():
    def __init__(self) -> None:
        self.methord={}
    def addMethod(self,oper:str,func):
        self.methord[oper]=func
    def calculate(self,calc:str):
        return self.methord[calc.split()[1]](eval(calc.split()[0]),eval(calc.split()[2]))
powerCalc = Calculator()
powerCalc.addMethod("*", lambda a,b :a * b)
powerCalc.addMethod("/", lambda a,b:a / b)
powerCalc.addMethod("**", lambda a,b:a ** b)

result = powerCalc.calculate("2 ** 3")
print( result ) # 8
