class a:
    def method(self):
        print("A class method")
        super().method()

class b:
    def method(self):
        print("B is class method")
        super().method()

class c:
    def method(self):
        print("C class method")

class x(a,b):
    def method(self):
        print("x class method")
        super().method()

class y(b,c):
    def method(self):
        print("y class method")
        super().method()

class z(x,y,c):
    def method(self):
        print("Z class method")
        super().mthod()