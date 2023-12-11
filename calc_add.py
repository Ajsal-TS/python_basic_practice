class Calculator():
    def __init__(self) -> None:
        pass
    def calculate(self,word):
        return eval(word)







calc = Calculator()

print( calc.calculate("3 + 7") )  # 10
print(calc.calculate("3-7"))