class calculation1:
    def summation(self,a,b):
        return a+b

class calculation2:
    def multiplication(self,a,b):
        return a*2

class devid(calculation1,calculation2):
    def divide(self,a,b):
        return a/b


d = devide()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))

    