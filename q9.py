class student:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setaddress(self,address):
        self.address=address
    def getaddress(self):
        return self.address
    def setmark(self,mark):
        self.mark=mark
    def getmark(self):
        return self.mark
    
s=student()
s.setid(10)
s.setname("raj")
s.setaddress("maninagar")
s.setmark(200)

print("ID",s.getid())
print("Name",s.getname())
print("Address",s.getaddress())
print("Marks",s.getmark())
