class myclass:
    n=0

    def myfunc(self):
        myclass.n = myclass.n+1

    def func():
        print("Number of instance:",myclass.n)

o1 = myclass()
o2 = myclass()
o3 = myclass()
o4 = myclass()
myclass.func()
