class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        last = self.name.split(" ")[0]
        return last
 
    @first_name.setter
    def first_name(self,last):
        parts = self.name.split(" ")
        new_name = f"{last} {parts[1]}" 
        self.name = new_name


e = Employee("Bilal Ahmed  Altaf",30000000)
print(e.first_name)
e.first_name ="Sumaid"
print(e.name)
