class Employee:
    Company = "Asus"
    def __init__(self,name,salary,Bond):
        self.name = name
        self.salary = salary
        self.Bond = Bond

    def  get_salary(self):
         return self.salary

    def get_info(self):
        print(f"The Name of the Employee  is {self.name}.His Salary is {self.salary} and his Bond is for {self.Bond} years ")

e = Employee("Sumaid Altaf",8000000000,4)
print(e.Company)
print(e.get_salary())
e.get_info()

