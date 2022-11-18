from email.mime import base
from re import L


class b1:
    def init(self):
        print("Base class b1")

class d1(b1):
    def init(self):
        super().init()
        print("Derived class1")

print("\n *** Using super's method ***")
o1 = d1()

class Base:
    def init(self):
        print("Base class b2")

class child1(base):
    def init(self):
        print("Derived class 3")

class child2(base):
    def init(self):
        print("Derived class 4")

print("\n *** Without using super() method ***")

b1 = base()
c1 = child1()
c2 = child2()