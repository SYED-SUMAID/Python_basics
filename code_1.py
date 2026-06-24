class Employee:
    Company = "Hp"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
#instance attribute
    def print_info(self):
        info = f"The name of the Employee is {self.name} and his salary is {self.salary} "
        return info
    @staticmethod 
    def product(numbers):
        result = 1
        for n in numbers:
            result *= n
        return result
    @classmethod
    def print_company(cls):
        print(cls.company)

    
    @classmethod
    def new_name(cls,new_company):
        cls.company = new_company    

e1 = Employee("Kara",50000)
e2 = Employee("Billy",66000)
print(e1.print_info())        
print(e2.print_info())        
# print(e1.average(7,9,4,5,67,7))
data = Employee.product([3,5,4,4])
print(data)
e1.new_name("Asus")
e1.print_company()