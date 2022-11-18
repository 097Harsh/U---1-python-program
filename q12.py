class details:
    def init(self):
        self.id = ()
        self.name = ""
        self.gender = ""

    def setDetails(self):
        self.id = int(input("Enter id:"))
        self.name = input("Enter name:")
        self.gender = input("Enter gender:")

    def showdetails(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Gender:",self.gender)

class employee(details):
    def init(self):
        self.company=""

    def setemployee(self):
        set.setDetails()
        self.company = input("Enter company name:")

    def showdetails(self):
        self.showdetails()
        print("Company:",self.company)

print("Employee object:")
e.employee()
e.setemployee()
e.showemployee()