class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a//b
a=int(input("enter a value"))
b=int(input("enter b value"))
obj=calculator()
result=obj.add(a,b)
print(f"Addition : {result}")
result=obj.sub(a,b)
print(f"Subtraction : {result}")
result=obj.mul(a,b)
print(f"Multiplication : {result}")
result=obj.div(a,b)
print(f"Divition : {result}")


